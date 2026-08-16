import java.io.* ;
import java.util.*;

import static java.lang.Math.* ;
import static java.util.Arrays.* ;

public class C {
	
	public static void main(String[] args) throws IOException {
		
		new C().solveProblem();
		
		out.close();
	}

	//static Scanner in = new Scanner(new InputStreamReader(System.in));
	static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	static PrintStream out = new PrintStream(new BufferedOutputStream(System.out));
	
	
	public void solveProblem() throws NumberFormatException, IOException {		

		int n =Integer.parseInt( in.readLine() );
		boolean[][] aan = new boolean[n][n] ;
		for( int i = 0 ; i < n ; i++ ){
			char[] c = in.readLine().toCharArray() ;
			
			for( int j = 0 ; j < n ; j++ )
				aan[i][j] = c[j]=='1' ;
		}
		
		boolean[] kolom = new boolean[n] ;
		boolean[] rij = new boolean[n] ;
		
		int a = 0 ;
		
		for( int i = n -1 ; i >= 0 ; i-- ){
			
			boolean ko = kolom[i] ;
			boolean ri = rij[i] ;
			rij[i] = false ;
			kolom[i] = false ;
			for( int j = 0 ; j <= i - 1 ; j++) {
				
				boolean nu = aan[j][i] ^ kolom[i] ^ rij[j] ;
				if( !nu )
					continue ;
				
				kolom[i] = !kolom[i] ;
				rij[j] = !rij[j] ;
		
		//		System.out.println((i+1) + " " + (j+1));
				a++ ;
				
			}
//			
//			for( int k = 0 ; k < n ; k++ )
//				for( int l = 0 ; l < n ; l++ ){
//					if( aan[k][l] ^ kolom[l] ^ rij[k] )
//						System.out.print(1);
//					else
//						System.out.print(0);
//					
//					if( l == n-1)
//						System.out.println();
//				}
			
			for( int j = 0 ; j <= i-1 ; j++) {
				
				boolean nu = aan[i][j] ^ kolom[j] ^ rij[i] ;
				if( !nu )
					continue ;

				
				
				rij[i] = !rij[i] ;
				kolom[j] = !kolom[j] ;

			//	System.out.println((i+1) + " " + (j+1));
				a++ ;
				
			}
			
			if( aan[i][i] ^ kolom[i] ^ rij[i] ^ko^ri)
				a++ ;
//			
//			for( int k = 0 ; k < n ; k++ )
//				for( int l = 0 ; l < n ; l++ ){
//					if( aan[k][l] ^ kolom[l] ^ rij[k] )
//						System.out.print(1);
//					else
//						System.out.print(0);
//					
//					if( l == n-1)
//						System.out.println();
//				}
		}
		out.println(a) ;
		
	}

       
}