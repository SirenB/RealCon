import pyvisa

class DIGISTANT4462( object ):

    def __init__( self, gpib_addr ):
        object.__init__( self )
        localResources = pyvisa.ResourceManager()
        #print(localResources.FindResources("?*"))
        self.ds = localResources.open_resource( "GPIB0::%i::INSTR" % gpib_addr )
        self.id = self.ds.query( "*IDN?" ).split( "\n", 1 ) [ 0 ]


    def shutDown( self ):
        if self.ds != None:
            self.ds.write( "SC 0UA" )
            self.ds.write( "LOCAL" )

    def getid( self ):
        return self.id

    def setI( self, value ):
        ''' set I on output to a given value (unit is micro Ampere) '''
        self.ds.write( "SC %iUA" % value )

    def curI( self ):
        ''' returns current I for the output '''
        value = self.ds.query( "SC?" ).split() [ 0 ]
        return int( float( value ) * 1000 )
