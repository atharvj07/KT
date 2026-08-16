

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */





import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import static java.lang.System.in;
import java.lang.reflect.Array;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.AbstractList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import static java.util.Collections.list;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import javax.xml.stream.events.Characters;





/**
 *
 * @author george
 */
public class main {
public static boolean isPrime(long n) {
    if(n < 2) return false;
    if(n == 2 || n == 3) return true;
    if(n%2 == 0 || n%3 == 0) return false;
    long sqrtN = (long)Math.sqrt(n)+1;
    for(long i = 6L; i <= sqrtN; i += 6) {
        if(n%(i-1) == 0 || n%(i+1) == 0) return false;
    }
    return true;
}

    private static long f(long l) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

static public class Princess{
 public int rate;public int beauty;public int intellect;public int richness;
 public Princess(int sum,int a,int b,int c){
  this.rate=sum;
  this.beauty=a;
  this.intellect=b;
  this.richness=c;
  }

        @Override
        public String toString() {
            return "Princess{" + "rate=" + rate + ", beauty=" + beauty + ", intellect=" + intellect + ", richness=" + richness + '}';
        }
 
 }
public static boolean contains(final int[] arr, final int key) {
    return Arrays.stream(arr).anyMatch(i -> i == key);
}
 static boolean isSubSequence(String str1, String str2, int m, int n)
    {
       
        if (m == 0) 
            return true;
        if (n == 0) 
            return false;
             
        
        if (str1.charAt(m-1) == str2.charAt(n-1))
            return isSubSequence(str1, str2, m-1, n-1);
 
        
        return isSubSequence(str1, str2, m, n-1);
    }

    static int gcdThing(int a, int b) {
    BigInteger b1 = BigInteger.valueOf(a);
    BigInteger b2 = BigInteger.valueOf(b);
    BigInteger gcd = b1.gcd(b2);
    return gcd.intValue();
}
    public static boolean checkAnagram(String str1, String str2) {
        int i=0;
        for (char c : str1.toCharArray()) {
        i = str2.indexOf(c, i) + 1;
        if (i <= 0) { return false; }
    }
    return true;

}
    /* Amusing Joke 
    String a,b,c;
     a=s.next();b=s.next();c=s.next();
     if((a.length()+b.length())!=c.length()){System.out.print("here");System.out.print("NO");}
     else{
         boolean x= true;
         String agex="";
         if(checkAnagram(a, c)==false){System.out.print("here1");x=false;}
         else{
             char [] g=a.toCharArray();
             Arrays.sort(g);String ge=new String(g);a=ge;
             g=b.toCharArray();Arrays.sort(g);ge=new String(b);b=ge;
             g=c.toCharArray();Arrays.sort(g);ge=new String(c);c=ge;
            if(isSubSequence(a, c, a.length(), c.length())){
                 StringBuilder sb = new StringBuilder(c);String temp="";
                for (int i = 0; i < a.length(); i++) {
                    temp+=a.charAt(i);
                 c.replaceFirst(temp, "");temp="";
                   
                }
            }
            else{x=false;}
            if(isSubSequence(a, c, a.length(), c.length())){
              StringBuilder sb = new StringBuilder(c);
                for (int i = 0; i < b.length(); i++) {
                  String temp="";
                    temp+=b.charAt(i);
                 c.replaceFirst(temp, "");temp="";
                   
                }
            }
            else{x=false;}
            if(c.length()!=0){x=false;}
    }if(x==false){System.out.print("NO");}
    else{System.out.print("YES");}
    }
    */
     /*//t,l,r
      long t,l,r;t=s.nextLong();l=s.nextLong();r=s.nextLong();
      long exp=0;
      // t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r).
        for (int i = 0; i <=r-l; i++) {
            exp+=((long)(Math.pow(t, i)))*f(l+i);
        }
        System.out.print(exp%(1000000007));*/
    /* 489C
        int digits=s.nextInt();int sum=s.nextInt();
        List <Integer>li=new ArrayList<Integer>();
       int digitss=sum/9;
       int rem=digits%9;
       String z=String.join("", Collections.nCopies(digitss, "9"));
       String z+=
       String digit="9";
       String x = String.join("", Collections.nCopies(digits, "9"));
       BigInteger num=BigInteger.valueOf(Long.parseLong(x));
       x=num.toString();System.out.print(x);
       li.clear();
        for (int i = 0; i < x.length(); i++) {
            li.add(x.charAt(i)-48);
        }
       Collections.sort(li);
       int zeros=0;
       //leading zeros
       String f="";
        for (int i = 0; i < li.size(); i++) {
            if(li.get(0)==0){zeros++;li.remove(0);}
            else{f=li.get(0).toString(); break;}
        }
        
        String y="";
        if(zeros!=0){
            li.remove(0);
            y+=String.join("", Collections.nCopies(zeros, "0"));
            
        }
       y+=li.stream().map(Object::toString).collect(Collectors.joining());
       System.out.print(y);System.out.print(" ");System.out.print(x);
    */
   
    public static void main (String []  args) throws IOException 
    {
        Scanner s=new Scanner(System.in);
        Long number=s.nextLong();
        String x=Long.toHexString(number);
        x=x.toUpperCase();
       long countCiclesInDigits=0;
       List<Character> L= x.chars().mapToObj(e->(char)e).collect(Collectors.toList());
       countCiclesInDigits=Collections.frequency(L, '9')+Collections.frequency(L, '0')+Collections.frequency(L, '4')+Collections.frequency(L, '6')+(Collections.frequency(L, '8')*2)+(Collections.frequency(L, 'B')*2)+Collections.frequency(L, 'D')+Collections.frequency(L, 'A');
     System.out.print(countCiclesInDigits);
    }
}    
  
