import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main
{
	public static void main(String[] args) {
		new Thread(null, new Runnable() {
			public void run() {
                solve();
            }
        }, "1", 1 << 26).start();
	}
	static void solve () {
		FastReader fr =new FastReader();	PrintWriter op =new PrintWriter(System.out);
 		
 		int t =fr.nextInt() ,m ,bx[] ,dm[] ,j ,l ,o ;	long n ,i ,k ,ans ;
 		while (t-- > 0) {
 			n =fr.nextLong() ;	m =fr.nextInt() ;	bx =new int[32] ;	dm =new int[32] ;	ans =0l ;
 			while (m-->0) {
 				i =fr.nextLong() ;	j =-1 ;
 				while (i>0l)	{	i>>=1l ;	++j ;	}	++bx[j] ;
 			}
 			while (n>0l) {
 				i =k =n&(-n) ;	j =-1 ;	while (i>0l)	{	i>>=1l ;	++j ;	}

 				for (l =Math.min(j,31) ; l>-1 ; --l) {
 					o =(int)Math.min(k/(1l<<l) , (long)bx[l]) ;
 					k -= ((1l<<l) * (long)o) ;	dm[l] =o ;
 				}
 				if (k==0l) {
 					for (l =Math.min(j,31) ; l>-1 ; --l)	bx[l] -= dm[l] ;
 					n &= (n-1l) ;	continue;
 				}
 				if (j<32) {
 					for (l =j+1 ; l<32 ; ++l) {
 						if (bx[l]!=0)	break;
 					}
 					if (l<32) {
 						--bx[l] ;	for (--l ; l>=j ; --l)	{	++bx[l] ;	++ans ;	}
 						--bx[j] ;	k =0l ;
 					}
 				}
 				if (k!=0l)	break;	n &= (n-1l) ;
 			}
 			if (n==0l)	op.println(ans) ;	else 	op.println("-1") ;
 		}
		op.flush();	op.close();
	}
	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br =new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st==null || (!st.hasMoreElements())) 
			{
				try
				{
					st =new StringTokenizer(br.readLine());
				}
				catch(IOException e)
				{
					e.printStackTrace();
				}
				
			}
			return st.nextToken();
		}

		String nextLine() {
			String str ="";

			try
			{
				str =br.readLine();
			}
			catch(IOException e)
			{
				e.printStackTrace();
			}

			return str;
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		long nextLong() {
			return Long.parseLong(next()) ;
		}
	}
}