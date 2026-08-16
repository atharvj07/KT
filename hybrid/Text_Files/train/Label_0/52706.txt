//package CROC2016;

import java.io.*;
import java.util.*;

/**
 * Created by brijesh on 10/8/16.
 */
public class Main {
    static double e_07=0.0000001;
    static int e09$7=1000000007;
    static final String[] EMPTY_ARRAY = new String[0];
    public static void main (String[] args) throws Exception {
        //BufferedReader br = new BufferedReader(new FileReader("/home/brijesh/Downloads/A-small-attempt0.in"));
        //BufferedReader br = new BufferedReader(new FileReader("/home/brijesh/Downloads/A-large.in"));
        //BufferedReader br = new BufferedReader(new FileReader("/home/brijesh/Downloads/C-small-practice.in"));
        //BufferedReader br = new BufferedReader(new FileReader("/home/brijesh/Downloads/C-large-practice.in"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        String[] day=new String[2];
        day[0]=br.readLine().trim();
        day[1]=br.readLine().trim();
        int[] d=new int[2];
        for(int i=0;i<2;i++){
            String s=day[i];
            if(s.equals("monday")) d[i]=1;
            else if(s.equals("tuesday")) d[i]=2;
            else if(s.equals("wednesday")) d[i]=3;
            else if(s.equals("thursday")) d[i]=4;
            else if(s.equals("friday")) d[i]=5;
            else if(s.equals("saturday")) d[i]=6;
            else if(s.equals("sunday")) d[i]=7;
        }
        if(d[1]<d[0]) d[1]+=7;
        int diff=d[1]-d[0];
        if(diff==0 || diff==2 || diff==3)
            System.out.println("YES");
        else System.out.println("NO");
        System.exit(0);
    }
}
