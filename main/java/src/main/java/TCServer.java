import py4j.GatewayServer;

public class TCServer {
    /** Class used to create a GatewayServer for the Python source files.
     * The gateway serves an instance of TextCategorization. */

    public static void main(String[] args){
        /** Server creation and start-up.*/

        GatewayServer server = new GatewayServer(new TextCategorization());
        System.out.println("Server started");
        server.start();
    }
}
