import py4j.GatewayServer;

public class JDSTServer {
    /**Server class that will use the GatewayServer object to permit python code to access the JVM and an instance of
     * the APIWrapper*/

    public static void main(String[] args) {
        /**Creates and starts a GatewayServer involving an APIWrapper instance*/

        GatewayServer server = new GatewayServer(new APIWrapper());
        System.out.println("Gateway server started");
        server.start();
        System.out.println("Gateway server finished");
    }
}
