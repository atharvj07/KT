import java.util.*;
import java.io.*;
import java.math.*;

public class mainClass
{	
	public static void main(String[] args)  throws IOException 
	{
		InputReader in = new InputReader(System.in);
		PrintWriter out = new PrintWriter(System.out);
	
        int n=in.nextInt();
       
        int max1=1,max2=1000000;

		for(int i=0;i<n;i++)
		{
			int x=in.nextInt();
			
			if(x>max1 && x<=500000)
				max1=x;
			
			if(x<max2 && x>500000)
				max2=x;
		}
		
		if(max1-1>1000000-max2)
		{out.println(max1-1);}
		else
		{out.println(1000000-max2);}
		
		out.flush();
		out.close();
	}

	static boolean isvow(char c)
    {
    	if(c=='a'|| c=='o'|| c=='i'|| c=='e'|| c=='u'|| c=='y')
    		return true;
    
    	return false;
    }
    
}
class InputReader{
    private final InputStream stream;
    private final byte[] buf=new byte[1024];
    private int curChar;
    private int numChars;
    public InputReader(InputStream stream){this.stream=stream;}
    private int read()throws IOException{
        if(curChar>=numChars){
            curChar=0;
            numChars=stream.read(buf);
            if(numChars<=0)
                return -1;
        }
        return buf[curChar++];
    }
    public final int nextInt()throws IOException{return (int)nextLong();}
    public final long nextLong()throws IOException{
        int c=read();
        while(isSpaceChar(c)){
            c=read();
            if(c==-1) throw new IOException();
        }
        boolean negative=false;
        if(c=='-'){
            negative=true;
            c=read();
        }
        long res=0;
        do{
            if(c<'0'||c>'9')throw new InputMismatchException();
            res*=10;
            res+=(c-'0');
            c=read();
        }while(!isSpaceChar(c));
        return negative?(-res):(res);
    }
    public final int[] readIntBrray(int size)throws IOException{
        int[] arr=new int[size];
        for(int i=0;i<size;i++)arr[i]=nextInt();
        return arr;
    }
    public final String next()throws IOException{
        int c=read();
        while(isSpaceChar(c))c=read();
        StringBuilder res=new StringBuilder();
        do{
            res.append((char)c);
            c=read();
        }while(!isSpaceChar(c));
        return res.toString();
    }
    public final String nextLine()throws IOException{
        int c=read();
        while(isSpaceChar(c))c=read();
        StringBuilder res=new StringBuilder();
        do{
            res.append((char)c);
            c=read();
        }while(c!='\n'&&c!=-1);
        return res.toString();
    }
    private boolean isSpaceChar(int c){
        return c==' '||c=='\n'||c=='\r'||c=='\t'||c==-1;
    }

}