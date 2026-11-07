LZ4 - Extremely fast compression
================================

LZ4 is a lossless compression algorithm,
providing compression speed > 500 MB/s per core,
scalable with multi-core CPUs.
It features an extremely fast decoder,
with speed in multiple GB/s per core,
typically reaching RAM speed limits on multi-core systems.

Compression speed can be tuned dynamically, by selecting an "acceleration" factor
which trades compression ratio for faster speed.
On the other end, a high compression derivative, LZ4_HC, is also provided,
trading CPU time for improved compression ratio.
All versions feature the same decompression speed.

LZ4 is also compatible with [dictionary compression](https://github.com/facebook/zstd#the-case-for-small-data-compression),
both at [API](lib/lz4frame.h) and [CLI](programs/lz4.1.md#operation-modifiers) (`-D`) levels.
It can ingest any input file as dictionary, though only the final 64 KB are used.
This capability can be combined with the [Zstandard Dictionary Builder](https://github.com/facebook/zstd/blob/dev/programs/zstd.1.md#dictionary-builder),
in order to drastically improve compression performance on small files.

The LZ4 library is provided as open-source software using the BSD 2-Clause license.
The `lz4` command line utility is provided under the GPL-2.0-or-later license.


Benchmarks
-------------------------

The benchmark uses [lzbench] v2.4.1, from @inikep
compiled with GCC v13.3.0 on Linux 64-bits (Ubuntu 24.04).
The reference system uses a Core i7-9700K CPU.
Benchmark evaluates the compression of reference [Silesia Corpus]
in single-thread mode.

[lzbench]: https://github.com/inikep/lzbench
[Silesia Corpus]: https://sun.aei.polsl.pl/~sdeor/index.php?page=silesia

|  Compressor             | Factor  | Compression | Decompression |
|  ----------             | -----   | ----------- | ------------- |
|  memcpy                 |  1.000  | 13700 MB/s  |  13700 MB/s   |
|**LZ4 default (v1.11.0)**|**2.112**| **770 MB/s**| **4950 MB/s** |
|

... (truncated)