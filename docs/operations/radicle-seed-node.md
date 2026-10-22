# Radicle Seed Node over Tor

How the project's Radicle seed node is set up as a Tor onion service ([ADR-0010](../decisions/ADR-0010-decentralized-source-and-site-hosting.md) §5). The steps follow chapter 4, "Embracing the Onion", of the [Radicle user guide](https://radicle.dev/guides/user); see it for details and updates.

## Why mixed mode

Radicle can use Tor in three ways:

| Mode | What goes through Tor | Use |
|---|---|---|
| **Mixed** (the project seed's mode) | Only connections to `.onion` addresses | The seed stays reachable on clearnet and as an onion service; clearnet peers see no added latency |
| Full proxy | All connections | An operator who must hide the node's IP address |
| Transparent proxy | All connections, through a Tor proxy the network already provides | Networks that already route everything through Tor |

The project seed is public infrastructure, so hiding its IP address is not the goal. Mixed mode adds an onion address that does not depend on one hosting provider's IP address or DNS, and it gives contributors who use Tor a direct route.

## 1. Onion service

Install Tor, then create the service directory with restricted permissions:

```bash
sudo mkdir -m 700 /var/lib/tor/radicle
```

Add to `/etc/tor/torrc`:

```text
HiddenServiceDir /var/lib/tor/radicle
HiddenServicePort 8776
```

`8776` is Radicle's default node port. Restart Tor, enable it at boot, and read the onion address:

```bash
sudo systemctl restart tor
sudo systemctl enable tor
sudo cat /var/lib/tor/radicle/hostname
```

Platform notes:
- **Debian packages:** if Tor cannot use the directory, run `sudo chown -R debian-tor:debian-tor /var/lib/tor/radicle`.
- **macOS:** install Tor with Homebrew and use `mkdir -p -m 700 ~/.tor/radicle`. The torrc is `/opt/homebrew/etc/tor/torrc`; set `HiddenServiceDir /Users/<user>/.tor/radicle`, restart with `brew services restart tor`, and read `~/.tor/radicle/hostname`.

Back up the `HiddenServiceDir`: its keys are the onion address. Losing them changes the address that the project published.

## 2. Radicle in mixed mode

Stop the node and edit its configuration:

```bash
rad node stop
rad config edit
```

Under `node`, route `.onion` addresses through Tor's SOCKS5 proxy, listen on the port the onion service forwards to, and advertise the onion address:

```json
"node": {
    "onion": {
        "mode": "proxy",
        "address": "127.0.0.1:9050"
    },
    "listen": ["0.0.0.0:8776"],
    "externalAddresses": [
        "<onion-address>.onion:8776"
    ]
}
```

The listen port must match `HiddenServicePort`. `externalAddresses` is optional: without it, peers that already know the onion address can still connect, but others cannot discover it. Then start the node:

```bash
rad node start
```

## 3. Connecting

Peers connect with `<NID>@<onion-address>.onion:8776`:

```bash
rad node connect <NID>@<onion-address>.onion:8776
```

To keep the connection across restarts, add the same address to `node.connect` in the peer's configuration. Building a Tor circuit takes a while, so the first connection can be slow.

## 4. Other modes

- **Full proxy:** set `node.proxy` to `127.0.0.1:9050`, and set `node.onion` to `{"mode": "forward"}` without an address. `listen` and `externalAddresses` stay as above. Every connection gains Tor latency.
- **Transparent proxy:** leave `node.proxy` unset and set `node.onion` to `{"mode": "forward"}`. The node then resolves `.onion` addresses through the operating system, which must already route traffic through Tor (see the Tor Project's documentation).

## 5. Publish

Once the canonical repository is seeded, publish in the README, CONTRIBUTING and the contributor page:

- the Repository ID (`rad:…`), which contributors clone with `rad clone`;
- the seed's Node ID (`rad self --nid`);
- the seed's onion address and its clearnet address.

## Security notes

- The upstream guide states that Radicle's codebase has not yet had a formal security audit. The seed holds no treasury or protocol authority (ADR-0006, ADR-0010).
- The seed's Radicle key is not a repository delegate key. Delegates merge from their own machines.
- Keep Tor and Radicle updated, and restrict the host's other open ports.
