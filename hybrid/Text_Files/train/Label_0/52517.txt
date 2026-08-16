import java.util.*;
import java.lang.*;
import java.io.*;

// Created by @thesupremeone on 30/06/21
public class GuardDuty {

    int r,b;

    void solve() throws IOException {
        r = getInt();
        b = getInt();
        if(r!=b){
            println("No");
            return;
        }
        println("Yes");
    }

    public static void main(String[] args) throws Exception {
        if (isOnlineJudge()) {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new BufferedWriter(new OutputStreamWriter(System.out));
            new GuardDuty().solve();
            out.flush();
        } else {
            localJudge = new Thread();
            in = new BufferedReader(new FileReader("input.txt"));
            out = new BufferedWriter(new FileWriter("output.txt"));
            localJudge.start();
            new GuardDuty().solve();
            out.flush();
            localJudge.suspend();
        }
    }
    static boolean isOnlineJudge(){
        try {
            return System.getProperty("ONLINE_JUDGE")!=null
                    || System.getProperty("LOCAL")==null;
        }catch (Exception e){
            return true;
        }
    }
    // Fast Input & Output
    static Thread localJudge = null;
    static BufferedReader in;
    static StringTokenizer st;
    static BufferedWriter out;
    static String getLine() throws IOException{
        return in.readLine();
    }
    static String getToken() throws IOException{
        if(st==null || !st.hasMoreTokens())
            st = new StringTokenizer(getLine());
        return st.nextToken();
    }
    static int getInt() throws IOException {
        return Integer.parseInt(getToken());
    }
    static long getLong() throws IOException {
        return Long.parseLong(getToken());
    }
    static void print(Object s) throws IOException{
        out.write(String.valueOf(s));
    }
    static void println(Object s) throws IOException{
        out.write(String.valueOf(s));
        out.newLine();
    }
}