import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String t = br.readLine();
        String p = br.readLine();
        for (int i = 0; i < t.length() - p.length() + 1; i++){
            if (t.substring(i, i + p.length()).equals(p)){
                System.out.println(i);
            }
        }
    }
}