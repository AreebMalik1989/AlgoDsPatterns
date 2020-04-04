package designpattern.structural.decorator;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Base64;
import java.util.zip.Deflater;
import java.util.zip.DeflaterOutputStream;
import java.util.zip.InflaterInputStream;

interface DataSource {
    void writeData(String data);
    String readData();
}

class FileDataSource implements DataSource {

    private String fileName;

    public FileDataSource(String fileName) {
        this.fileName = fileName;
    }

    @Override
    public void writeData(String data) {
        
        File file = new File(fileName);

        try(OutputStream fos = new FileOutputStream(file)) {
            fos.write(data.getBytes(), 0, data.length());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String readData() {

        char[] buffer = null;
        File file = new File(fileName);
        try(FileReader reader = new FileReader(file)) {
            buffer = new char[(int) file.length()];
            reader.read(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }

        return new String(buffer);
    }
}

class DataSourceDecorator implements DataSource {

    private DataSource wrappee;

    public DataSourceDecorator(DataSource source) {
        wrappee = source;
    }

    @Override
    public void writeData(String data) {
        wrappee.writeData(data);
    }

    @Override
    public String readData() {
        return wrappee.readData();
    }
}

class EncryptionDecorator extends DataSourceDecorator {

    public EncryptionDecorator(DataSource source) {
        super(source);
    }

    @Override
    public void writeData(String data) {
        super.writeData(encode(data));
    }

    @Override
    public String readData() {
        return decode(super.readData());
    }

    private String encode(String data) {
        byte[] result = data.getBytes();
        for(int i=0; i<result.length; i++) {
            result[i] += (byte) 1;
        }
        return Base64.getEncoder().encodeToString(result);
    }

    private String decode(String data) {
        byte[] result = Base64.getDecoder().decode(data);
        for(int i=0; i<result.length; i++) {
            result[i] -= (byte) 1;
        }
        return new String(result);
    }
}

class CompressionDecorator extends DataSourceDecorator {

    private int compLevel = 6;

    public CompressionDecorator(DataSource source) {
        super(source);
    }

    @Override
    public void writeData(String data) {
        super.writeData(compress(data));
    }

    @Override
    public String readData() {
        return decompress(super.readData());
    }

    public int getCompressionLevel() {
        return compLevel;
    }

    public void setCompressionLevel(int compLevel) {
        this.compLevel = compLevel;
    }

    private String compress(String stringData) {
        
        byte[] data = stringData.getBytes();
        
        try(ByteArrayOutputStream bout = new ByteArrayOutputStream(512);
            DeflaterOutputStream dos = new DeflaterOutputStream(bout, new Deflater(compLevel))) {
            
            dos.write(data);
            return Base64.getEncoder().encodeToString(bout.toByteArray());

        } catch(IOException e) {
            return null;
        }
    }

    private String decompress(String stringData) {

        byte[] data = Base64.getDecoder().decode(stringData);
        try(InputStream in = new ByteArrayInputStream(data);
            InflaterInputStream iis = new InflaterInputStream(in);
            ByteArrayOutputStream baos = new ByteArrayOutputStream(512)) {

                int b;
                while((b = iis.read()) != -1) {
                    baos.write(b);
                }

                return new String(baos.toByteArray());
        } catch(IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}

class Demo {
    public static void main(String[] args) {
        String salaryRecords = "Name,Salary\nJohn Smith,100000\nSteven Jobs,912000";
        DataSourceDecorator encoded = new CompressionDecorator(
                                        new EncryptionDecorator(
                                            new FileDataSource("out/Output.txt")));

        encoded.writeData(salaryRecords);

        DataSource plain = new FileDataSource("out/Output.txt");

        System.out.println("- Input ----------------");
        System.out.println(salaryRecords);
        System.out.println("- Encoded --------------");
        System.out.println(plain.readData());
        System.out.println("- Decoded --------------");
        System.out.println(encoded.readData());

        /*
         * Output:
         * - Input ----------------
         * Name,Salary
         * John Smith,100000
         * Steven Jobs,912000
         * - Encoded --------------
         * Zkt7e1Q5eU8yUm1Qe0ZsdHJ2VXp6dDBKVnhrUHtUe0sxRUYxQkJIdjVLTVZ0dVI5Q2IwOXFISmVUMU5rcENCQmdxRlByaD4+
         * - Decoded --------------
         * Name,Salary
         * John Smith,100000
         * Steven Jobs,912000
         */
    }
}