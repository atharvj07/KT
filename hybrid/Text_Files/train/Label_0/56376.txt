import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            List<String> input = Arrays.<String>asList(sc.nextLine().split(""));
            // List<String> input =
            // Arrays.<String>asList("@99+1=1@90".split(""));
            System.out.println(decoding(input));
        }
    }

    private static String decoding(List<String> list) {
        StringBuilder sb = new StringBuilder();

        String s = "";
        int roop = 0;
        for (int i = 0; i < list.size(); i++) {
            s = list.get(i);
            if ("@".equals(s)) {
                roop = Integer.parseInt(list.get(i + 1));
                i++;
                for (int j = 0; j < roop; j++) {
                    sb.append(list.get(i + 1));
                }
                i++;
            } else {
                sb.append(s);
            }
        }
        return sb.toString();
    }
}