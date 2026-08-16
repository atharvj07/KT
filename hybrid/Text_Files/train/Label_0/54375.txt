//package codeforces;

import java.util.Scanner;

/**
 * Created by nitin.s on 03/08/17.
 */
public class TextVolume {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        String s = in.nextLine();
        String[] split = s.split(" ");
        int answer = 0;
        for(String str: split) {
            int local = 0;
            for(int i = 0; i < str.length(); ++i) {
                if(str.charAt(i) >= 'A' && str.charAt(i) <= 'Z') ++local;
            }
            answer = Math.max(answer, local);
        }
        System.out.println(answer);
    }
}
