import java.util.Arrays;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int[] cnt = new int[150];
        long ans = 0;
        Map<String, Long> map = new TreeMap<>();
        Long val;
        String tmp;
        char[] c = new char[2];  //长度为二字串的
        for (int i = 0; i < s.length(); i++) {  //与之前出现过的字符组成长度为二的字符串进行比较
            c[1] = s.charAt(i);
            for (int j = 0; j < 26; j++) {
                c[0] = (char) ('a' + j);
                tmp = Arrays.toString(c);  //长度为2的子串
                val = map.get(tmp);
                if (val == null)
                    val = 0L;
                if (cnt[c[0]] > 0)
                    val += cnt[c[0]];
                map.put(tmp, val);
                if (val > ans) {
                    ans = val;
                    //System.out.println("index:" + i + " tmp" + tmp);
                }
            }
            ++cnt[c[1]];
            if (cnt[c[1]] > ans) {
                ans = cnt[c[1]];
                //System.out.println("index:" + i + " cnt[" + c[1] + "] = " + ans);
            }

        }
        System.out.println(ans);
    }
}

