import java.awt.*;
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        Scanner sc=new Scanner(System.in);
        int v1=sc.nextInt(),v2=sc.nextInt(),t=sc.nextInt(),d=sc.nextInt(),sum=0;
        for (int i=0;i<t;i++)sum+=Math.min(v1+d*i,v2+(t-1-i)*d);
        System.out.println(sum);
    }
}