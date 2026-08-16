
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Madi
 */
public class B462 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = sc.nextInt();
        int k = sc.nextInt();

        String s = sc.next();
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[(int)s.charAt(i) - 65]++;
        }
        
        for (int i = 0; i < 25; i++) {
            for (int j = i + 1; j < 26; j++) {
                if (cnt[i] < cnt[j]) {
                    int t = cnt[i];
                    cnt[i] = cnt[j];
                    cnt[j] = t;
                }
            }
        }
        
        int ind = 0;
        long sum = 0;
        while (ind < 26 && k > cnt[ind]) {
            k -= cnt[ind];
            sum += (long)cnt[ind] * (long)cnt[ind];
            ind++;
        }
        
        sum += (long)k * (long)k;
        bw.write(sum + "\n");
        bw.flush();
    }
}
