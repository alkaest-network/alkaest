# Alkaest Search

## Purpose

Alkaest Search lets anyone find professionals on the Alkaest network (for example "barbeiro hoje à tarde perto do centro") and book with them, ranked by verifiable reputation instead of paid placement.

It is the evolution of the **WhatsApp Discovery Number** described in `chatbot-to-network-strategy.md`.

**Launch policy: stealth.** Alkaest Search is built and tested privately and is not announced until there are enough providers to give useful answers. Launching with empty results would burn the first impression.

---

## Launch Gate

Search opens publicly per region and per service category, only when that combination has enough supply. Suggested starting thresholds (tune with real data):

* at least 10 active providers in the category within the region;
* at least 70% of searches in internal testing return three or more bookable options within 24 hours;
* providers have reputation evidence (rated appointments) to rank on.

Until a region passes the gate, the search is available only to an allowlist of testers.

---

## Evolution

| Stage | Where the index lives | Who can search |
|---|---|---|
| 1. Private catalog | The chatbot operator's database, built from paying chatbot clients | Allowlisted testers, through a private WhatsApp number |
| 2. Discovery number | Same catalog, plus availability from each provider's calendar | Public, region by region, after the launch gate |
| 3. Network search | Indexes on service nodes, built from listings providers publish to the network | Anyone running a node or app; also the WhatsApp number as a gateway |

Stage 1 can start as soon as the chatbot has clients; nothing about it is public.

---

## Network Search Design (Stage 3)

1. **Listings are signed objects.** Each provider publishes a listing object in its own space: services (with durations and price ranges), coarse location (a geohash prefix, not an address), languages, and an availability summary. Listings are public business data.
2. **Discovery by key.** Listings are announced in the DHT under keys derived from `(service category, geohash prefix)`, so a node can find providers in an area without a central index.
3. **Indexers speed things up.** Service nodes (ADR-0003) build full-text and geographic indexes over the listings they collect. An indexer can omit results but cannot forge them, because every result is a signed listing.
4. **Clients do not trust one indexer.** A light client asks several indexers, merges the results, verifies signatures, and discards anything stale.
5. **Ranking is reproducible.** Results are ranked by reputation computed from signed evidence (RFC-0006) and by availability fit. Any node can recompute a ranking; no paid placement.
6. **Booking goes to the provider.** The search only finds; the booking is a request to the provider's own node (or its chatbot), which owns its calendar.
7. **Searchers stay private.** Queries can travel through relays or Tor; searching does not require an identity, and booking reveals only what the provider needs.

---

## Open Questions

* How coarse should public location be (city, neighbourhood, geohash precision) so customers can judge distance without exposing home-based professionals?
* Should availability summaries be published (privacy and freshness cost) or only fetched on demand from the provider's node?
* Anti-spam for listings: rate limits per identity, minimum identity age, or a small bond (see ADR-0004).
