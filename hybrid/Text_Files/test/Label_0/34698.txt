import static java.lang.System.*;
import static java.lang.Math.*;

import java.lang.reflect.Array;
import java.util.*;
import java.util.Map.Entry;

public class C305 {
    public static Scanner sc=new Scanner(in);
    //public static Random sc=new Random();

    void run() {
        final int n=sc.nextInt();
        int[] as=new int[n];
        for(int i = 0; i < n; i++) as[i]=sc.nextInt();

        int tcnt=0,tmax=0;
        for(int i=0;i<n;){
            int j =i;
            while (j+1 < n && as[i]==as[j+1]) j++;
            int cnt=j-i+1;
            if (cnt % 2 == 1){// is 1
                tcnt++;
                if (as[i] > tmax) tmax = as[i];
                i++;
            }
            // carry up
            cnt/=2;
            i += cnt;
            for(int k = j; k>j-cnt;k--) as[k]++;
        }
        ln(tmax-tcnt+1);
    }

    public static void main(String[] args) {
        new C305().run();
    }


    //output lib
    static final String br=System.getProperty("line.separator");
    static final String[] asep=new String[]{""," ",br,br+br};


    static String str(Object o){
        int depth=_getArrayDepth(o);
        return depth>0?_strArray(o,depth):o.toString();
    }
    @Deprecated
    static int _getArrayDepth(Object o){
        if(!o.getClass().isArray() || Array.getLength(o)==0) return 0;
        return  1+_getArrayDepth(Array.get(o,0));
    }
    @Deprecated
    private static String _strArray(Object o,int depth){
        if(depth==0) return str(o);
        StringBuilder sb=new StringBuilder();
        for(int i=0,len=Array.getLength(o);i<len;i++){
            if(i!=0)sb.append(asep[depth]);
            sb.append(_strArray(Array.get(o,i),depth-1));
        }
        return sb.toString();
    }

    public static void pr(Object obj){
        out.print(str(obj));
    }
    public static void ln(){
        out.println();
    }
    public static void ln(Object... obj){
        for(Object o:obj){
            pr(o);ln();
        }
    }
}
