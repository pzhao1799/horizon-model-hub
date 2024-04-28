import fsspec

class HorizonFileSystem(fsspec.AbstractFileSystem):
    """
    Access a remote Horizon Hub repository as if were a local file system.
    """

    def __init__(self, *args, **storage_options):
        super().__init__(*args, **storage_options)
     

