package designpattern.structural.adapter;

interface IBluetoothTransmitter {
    void transmit(String msg);
}

interface IWifiTransmitter {
    void send(String msg);
}

interface Messenger {
    void sendMessage(IWifiTransmitter wifiTransmitter, String msg);
}

class BluetoothTransmitter implements IBluetoothTransmitter {
    @Override
    public void transmit(String msg) {
        System.out.println("Transmitting message over bluetooth.");
    }
}

class WifiTransmitter implements IWifiTransmitter {
    @Override
    public void send(String msg) {
        System.out.println("Sending message over wifi.");
    }
}

class WifiAdapter implements IWifiTransmitter {

    private IBluetoothTransmitter bluetoothTransmitter;

    public WifiAdapter(IBluetoothTransmitter bluetoothTransmitter) {
        this.bluetoothTransmitter = bluetoothTransmitter;
    }

    @Override
    public void send(String msg) {
        bluetoothTransmitter.transmit(msg);
    }
}

class WifiMessenger implements Messenger {
    @Override
    public void sendMessage(IWifiTransmitter wifiTransmitter, String msg) {
        System.out.println("Wifi messenger sending message.");
        wifiTransmitter.send(msg);
    }
}

public class Adapter {

    public static void main(String args[]) {

        String msg = "Hello";

        IWifiTransmitter wifiTransmitter = new WifiTransmitter();
        IBluetoothTransmitter bluetoothTransmitter = new BluetoothTransmitter();

        WifiAdapter wifiAdapter = new WifiAdapter(bluetoothTransmitter);
        
        WifiMessenger wifiMessenger = new WifiMessenger();
        wifiMessenger.sendMessage(wifiTransmitter, msg);
        wifiMessenger.sendMessage(wifiAdapter, msg);
    }
}