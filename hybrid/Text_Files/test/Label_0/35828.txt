
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author root
 */
public class A {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int c = in.nextInt();
        int p[] = new int[n];
        int t[] = new int[n];
        for (int i = 0; i < n; i++) {
            p[i] = in.nextInt();
        }
        for (int i = 0; i < n; i++) {
            t[i] = in.nextInt();
        }

        long l = 0;
        long time = 0;
        for (int i = 0; i < n; i++) {
            time += t[i];
            long points = p[i] - time * c;
            l += (points>0)?points:0;
        }

        long r = 0;
        time = 0;
        for (int i = n - 1; i >= 0; i--) {
            time += t[i];
            long points = p[i] - time * c;
            r += (points>0)?points:0;
        }
//        System.out.println(l+" "+r);    
                
        if(r<l){
            System.out.println("Limak");
        } else if(l<r){
            System.out.println("Radewoosh");
        } else {
            System.out.println("Tie");
        }
    }
}
