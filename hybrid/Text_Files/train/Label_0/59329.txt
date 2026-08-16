import java.util.*;
import java.io.*;
import java.math.*;

public class Main {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String str=sc.next();
        BigInteger a=new BigInteger(str);
        str=sc.next();
        BigInteger b=new BigInteger(str);
        System.out.println(a.divide(b));
    }
}

