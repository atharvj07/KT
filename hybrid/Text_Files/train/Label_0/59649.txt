import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class First {
    public static void main(String[] args) {
        String string = "";
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            int n = Integer.parseInt(reader.readLine());
            string = reader.readLine();
            reader.close();
        }catch (IOException e)
        {
            System.out.println(e.getStackTrace());
        }

        ArrayList<Integer> list = new ArrayList<>();

        int count = 0;
        String[] strs = string.split("[W]+");
        for (String s:strs) {
            if (s.length() != 0) {
                count++;
                list.add(s.length());
            }
        }


        System.out.println(count);
        for (int i:list) {
                System.out.print(i + " ");
        }
    }
}