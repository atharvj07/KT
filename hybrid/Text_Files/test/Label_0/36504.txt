
import java.util.Arrays;
import java.util.Scanner;

public class E {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int n = in.nextInt();

        String[] p = new String[n];
        String[] s = new String[n];

        int pc[] = new int[26];
        int sc[] = new int[26];

        for (int i = 0; i < n; i++) {
            p[i] = in.next();
            pc[p[i].charAt(0) - 'A']++;
        }

        for (int i = 0; i < n; i++) {
            s[i] = in.next();
            sc[s[i].charAt(0) - 'A']++;
        }

        Arrays.sort(p);
        Arrays.sort(s);


        int match[] = new int[n];
        
        boolean[] ms = new boolean[n];


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!ms[j]) {
                    if (p[i].charAt(0) == s[j].charAt(0)) {
                        ms[j] = true;
                        match[i] = j;
                        break;
                    }
                    if( pc[p[i].charAt(0)-'A'] > sc[p[i].charAt(0)-'A'] && pc[s[j].charAt(0)-'A'] < sc[s[j].charAt(0)-'A'] ){
                        ms[j] = true;
                        match[i] = j;
                        break;
                    }
                }
            }
            pc[p[i].charAt(0)-'A']--;
            sc[s[match[i]].charAt(0)-'A']--;
        }



        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < n - 1; i++) {
            sb.append(p[i] + " " + s[match[i]] + ", ");
        }
        sb.append(p[n - 1] + " " + s[match[n - 1]]);

        System.out.println(sb.toString());
    }
}
