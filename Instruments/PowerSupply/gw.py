import pyvisa

class gw( object ):

    def __init__( self, gpib_addr ):
        object.__init__( self )
        localResources = pyvisa.ResourceManager()
        #print(localResources.FindResources("?*"))
        self.addr = gpib_addr
        self.ql = localResources.open_resource( "GPIB0::%i::INSTR" % gpib_addr )
        self.id = self.ql.query( "*IDN?" ).split( "\n", 1 ) [ 0 ]


    def shutDown( self ):
        if self.ql != None:
            self.outOff()
            self.ql.write( "LOCAL" )

    def getid( self ):
        return self.id

    def setV( self, value ):
        #set V output to a given value
        self.ql.write( "V1 %f" % value )

    def setIlim( self, value ):
        ''' set I limit on output to a given value '''
        self.ql.write( "I1 %f" % value )

    def outOn( self ):
        ''' turns ON the output '''
        self.ql.write( "OP1 1" )

    def outOff( self ):
        ''' turns OFF the output '''
        self.ql.write( "OP1 0 ")

