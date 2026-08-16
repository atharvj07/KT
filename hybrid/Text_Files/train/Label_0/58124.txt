/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author BATCH1
 */
import java.util.*;
public class ques1 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int c= 0;
        String s = sc.next();
        for(int i =0;i<n;i++)
            if(s.charAt(i)=='1')
                c++;
        if(c*2!=n){
            System.out.println(1);
            System.out.println(s);
        }
        else{
            System.out.println(2);
            System.out.println(s.substring(0,1) + " " + s.substring(1));
        }
    }
}
