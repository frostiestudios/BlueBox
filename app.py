from aiopmtiles import Reader

async with Reader("https://r2-public.protomaps.com/protomaps-sample-datasets/cb_2018_us_zcta510_500k.pmtiles") as src:
    # PMTiles Metadata
    meta = src.metadata

    # Spatial Metadata
    bounds = src.bounds
    minzoom, maxzoom = src.minzoom, src.maxzoom

    # Is the data a Vector Tile Archive
    assert src.is_vector

    # PMTiles tiles type
    tile_type = src._header["tile_type"]

    # Tile Compression
    comp = src.tile_compression

    # Get Tile
    data = await src.get_tile(0, 0, 0)