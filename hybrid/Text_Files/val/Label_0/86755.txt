import java.util.*;
import java.io.*;
public class Main {
    
    static class Scan {
        private byte[] buf=new byte[1024];
        private int index;
        private InputStream in;
        private int total;
        public Scan()
        {
            in=System.in;
        }
        public int scan()throws IOException
        {
            if(total<0)
            throw new InputMismatchException();
            if(index>=total)
            {
                index=0;
                total=in.read(buf);
                if(total<=0)
                return -1;
            }
            return buf[index++];
        }
        public int scanInt()throws IOException
        {
            int integer=0;
            int n=scan();
            while(isWhiteSpace(n))
            n=scan();
            int neg=1;
            if(n=='-')
            {
                neg=-1;
                n=scan();
            }
            while(!isWhiteSpace(n))
            {
                if(n>='0'&&n<='9')
                {
                    integer*=10;
                    integer+=n-'0';
                    n=scan();
                }
                else throw new InputMismatchException();
            }
            return neg*integer;
        }
        public double scanDouble()throws IOException
        {
            double doub=0;
            int n=scan();
            while(isWhiteSpace(n))
            n=scan();
            int neg=1;
            if(n=='-')
            {
                neg=-1;
                n=scan();
            }
            while(!isWhiteSpace(n)&&n!='.')
            {
                if(n>='0'&&n<='9')
                {
                    doub*=10;
                    doub+=n-'0';
                    n=scan();
                }
                else throw new InputMismatchException();
            }
            if(n=='.')
            {
                n=scan();
                double temp=1;
                while(!isWhiteSpace(n))
                {
                    if(n>='0'&&n<='9')
                    {
                        temp/=10;
                        doub+=(n-'0')*temp;
                        n=scan();
                    }
                    else throw new InputMismatchException();
                }
            }
            return doub*neg;
        }
        public String scanString()throws IOException
        {
            StringBuilder sb=new StringBuilder();
            int n=scan();
            while(isWhiteSpace(n))
            n=scan();
            while(!isWhiteSpace(n))
            {
                sb.append((char)n);
                n=scan();
            }
            return sb.toString();
        }
        private boolean isWhiteSpace(int n)
        {
            if(n==' '||n=='\n'||n=='\r'||n=='\t'||n==-1)
            return true;
            return false;
        }
    }
    
    public static void main(String args[]) throws IOException {
        Scan input=new Scan();
        int n=input.scanInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++) {
            arr[i]=input.scanInt();
        }
        int strt[]=new int[2*n];
        int end[]=new int[2*n];
        int indx=0;
        for(int i=0;i<n;i++) {
            strt[indx]=i;
            while(i<n-1 && arr[i]<arr[i+1]) {
                i++;
            }
            end[indx]=i;
            indx++;
        }
        if(end[indx-1]!=n-1) {
            strt[indx]=end[indx]=n=1;
            indx++;
        }
        int max=0;
        for(int i=0;i<indx;i++) {
//            System.out.println(strt[i]+" "+end[i]);
            max=Math.max(max,end[i]-strt[i]+1);
        }
        for(int i=0;i<indx-1;i++) {
            if(end[i]+2==strt[i+1] && arr[strt[i+1]]>arr[end[i]]) {
                max=Math.max(max,(end[i]-strt[i]+1)+(end[i+1]-strt[i+1]+1));
            }
            if(end[i]+1==strt[i+1] && end[i]-1>=0 && arr[strt[i+1]]>arr[end[i]-1]) {
                max=Math.max(max,(end[i]-strt[i]+1)+(end[i+1]-strt[i+1]+1)-1);
            }
            if(end[i]+1==strt[i+1] && strt[i+1]+1<n && arr[strt[i+1]+1]>arr[end[i]]) {
                max=Math.max(max,(end[i]-strt[i]+1)+(end[i+1]-strt[i+1]+1)-1);
            }
        }
        System.out.println(max);
    }
}
