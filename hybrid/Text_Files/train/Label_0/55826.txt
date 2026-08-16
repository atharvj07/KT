import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class CodeForces {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long x = Long.parseLong(st.nextToken());
        long k = Long.parseLong(st.nextToken());



        long[] a=new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            long element=Long.parseLong(st.nextToken());
            a[i]=element;
        }


        Arrays.sort(a);

        long ans=0;
        for (int i = 0; i < n; i++) {
            long l,r;
            if (a[i]%x!=0){
                l=Math.max(x*(a[i]/x) + (k*x),a[i]);
                r=x*(a[i]/x) + (((k+1)*x)-1);
            }else{
                l=Math.max(x*(a[i]/x) + ((k-1)*x),a[i]);
                r=x*(a[i]/x) + ((k*x)-1);
            }
            if (r>=l){
                ans+=findIndexOfNumbersInTheRange(l,r,a);
            }
        }
        System.out.println(ans);
    }

    private static int findIndexOfNumbersInTheRange(long l, long r, long[] a){

        //find the first occurrence of number greater than equal to l
        int indexL=binarySearchFindFirstOccurrence(a,l);
        //find the last occurrence of number less than equal to r
        int indexR=binarySearchFindLastOccurrence(a,r);

        if (indexL!=-1 && indexR!=-1 && (indexR-indexL+1)>0){
            return (indexR-indexL+1);
        }
        return 0;
    }

    private static int binarySearchFindFirstOccurrence(long[] a,long element){
        int l=0;
        int h=a.length-1;

        while(l<h){
            int m=(h+l)/2;
            if (a[m]<element){
                l=m+1;
            }else{
                h=m;
            }
        }

        if (a[h]<element){
            return -1;
        }
        return h;
    }
    private static int binarySearchFindLastOccurrence(long[] a,long element){
        int l=0;
        int h=a.length-1;

        while(l<=h){
            int m=(h+l)/2;
            if (a[m]<element){
                l=m+1;
            }else if (a[m]==element){
                if (m==a.length-1){
                    return m;
                }
                if (element<a[m+1]) {
                    return m;
                }else{
                    l=m+1;
                }
            }else{
                h=m-1;
            }
        }

        if (h>=0 && h<=a.length-1 && a[h]<element){
            return h;
        }else{
            return -1;
        }
    }
}