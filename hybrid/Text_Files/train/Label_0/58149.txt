import java.util.*;
import java.util.*; import java.lang.*; import java.io.*;


public class s{
   
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        ArrayList<String>ar = new ArrayList<String>();
        int n = t/2,o = 1;
        for(int r=1;r<=t/2;r++){
            String s="";
            for(int i = 1;i<=n;i++)
                s=s+"*";
            for(int j = 1;j<=o;j++)
                s=s+"D";
            for(int k = 1;k<=n;k++)
                s=s+"*";
            System.out.println(s);
            ar.add(s);
            n = n-1;
            o=o+2;
        }
        for(int i = 1;i<=t;i++)
            System.out.print("D");
        System.out.println();
        for(int i = ar.size()-1;i>=0;i--)
            System.out.println(ar.get(i));
    }
}