package designpattern.structural.proxy;

interface Server {
    void request();
}

class RealServer implements Server {
    @Override
    public void request() {
        System.out.println("RealSubject: Handling request");
    }
}

class ProxyServer implements Server {

    private Server realServer;

    public ProxyServer(Server realServer) {
        this.realServer = realServer;
    }

    @Override
    public void request() {
        if(checkAccess()) {
            realServer.request();
            logRequest();
        }
    }

    private boolean checkAccess() {
        System.out.println("Proxy: Checking access prior to firing a real request.");
        return true;
    }

    private void logRequest() {
        System.out.println("Proxy: Logging the time of request.");
    }
}

class Client {
    
    private Server server;

    public Client(Server server) {
        this.server = server;
    }

    public void request() {
        server.request();
    }
}

public class Proxy {

    public static void main(String args[]) {
        
        System.out.println("Client: Executing the code with real server");
        Server realServer = new RealServer();
        Client client = new Client(realServer);
        client.request();

        System.out.println();

        System.out.println("Client: Executing the code with proxy server");
        Server proxyServer = new ProxyServer(realServer);
        client = new Client(proxyServer);
        client.request();
    }
}