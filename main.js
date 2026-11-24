// One Sentence for a Traveler from 1800 — make.fun entry program.
//
// Writes a single sentence (125 characters) to /output/entry.txt that
// explains the modern internet to someone who has just stepped out of
// the year 1800, using only words and pictures that person could hold
// in their head: a harbour, ships from every shore, letters, songs and
// gossip arriving at your door, faster than any horse could ride.
//
// Deterministic: the same bytes on every run, no input, no clock, no
// randomness. The output directory is created if it does not exist.
// No trailing newline: the file holds exactly the sentence, nothing else.

const fs = require("node:fs");
const path = require("node:path");

const ENTRY =
  "It is a harbour where ships from every shore unload letters, songs " +
  "and gossip at your door, faster than any horse could ride.";

function main() {
  const outDir = "/output";
  const outFile = path.join(outDir, "entry.txt");
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(outFile, ENTRY, "utf8");
  const written = fs.readFileSync(outFile, "utf8");
  if (written !== ENTRY) {
    throw new Error("entry.txt does not match the expected sentence");
  }
  if (written.length > 200 || written.length < 1) {
    throw new Error("entry length outside the 1-200 character gate");
  }
}

main();
