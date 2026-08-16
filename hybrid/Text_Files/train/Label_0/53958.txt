import java.io.*;
import java.lang.Math;
import java.util.Scanner;

public class main
{
        public static Scanner in;
        public static PrintStream out;
       
        public static void test()
        {
                int ti = in.nextInt();
                int td = in.nextInt();
                int tr = in.nextInt();
                int te = in.nextInt();
               
                in.nextLine();
               
                String A = in.nextLine();
               
                if (A.length()==0)
                {
                        A = in.nextLine();
                }
               
                String B = in.nextLine();
               
                int N = A.length();
                int M = B.length();
				
				int i,j,k;
				
				int[][] last_a = new int[26][];
				int[][] last_b = new int[26][];
				char c;
				for (c='a'; c<='z'; c++)
				{
					last_a[c-'a'] = new int[N+1];
					last_b[c-'a'] = new int[M+1];
					
					last_a[c-'a'][0] = 0;
					last_b[c-'a'][0] = 0;
					
					for (j=0; j<N;j++)
					{
						if (A.charAt(j)==c)
						{
							last_a[c-'a'][j+1] = j+1;
						}
						else
						{
							last_a[c-'a'][j+1] = last_a[c-'a'][j];
						}
					}
					
					for (j=0; j<M;j++)
					{
						if (B.charAt(j)==c)
						{
							last_b[c-'a'][j+1] = j+1;
						}
						else
						{
							last_b[c-'a'][j+1] = last_b[c-'a'][j];
						}
					}
				}
				
                int t[][] = new int[N+1][];
                for (i=0; i<=N; i++)
                {
                        t[i] = new int[M+1];
                }
               
                t[0][0] = 0;
                for (i=1; i<=N; i++)
                {
                        t[i][0] = td * i;
                }
                for (j=1; j<=M; j++)
                {
                        t[0][j] = ti * j;
                }
               
                int m,x,y;
                for (i=1; i<=N; i++)
                {
                        for (j=1;j<=M;j++)
                        {
                                m = tr + t[i-1][j-1];
                       
                                if (A.charAt(i-1) == B.charAt(j-1))
                                {
                                        m = Math.min(m, t[i-1][j-1]);
                                }
                               
                                m = Math.min(m, td + t[i-1][j]);
                                m = Math.min(m, ti + t[i][j-1]);
                              /*
                                if ((i>1)&&(j>1)&&(A.charAt(i-1) == B.charAt(j-2))&&(A.charAt(i-2) == B.charAt(j-1)))
                                {
                                        m = Math.min(m, te + t[i-2][j-2]);
                                }
                               */
							   
								if ((i>1)&&(j>1))
								{
									x = last_a[B.charAt(j-1)-'a'][i-1];
									y = last_b[A.charAt(i-1)-'a'][j-1];
									
									if ((x>0)&&(y>0))
									{
										m = Math.min(m, td*(i-x-1)+ti*(j-y-1)+te + t[x-1][y-1]);
									}
								}
							   
                                t[i][j] = m;                            
                        }
                }
               
                out.println(t[N][M]);
        }
       
        public static void main(String args[])
        {
                try
                {
                        //in = new Scanner(new File("in.txt"));
                        //out = new PrintStream(new File("out.txt"));                  
                        in = new Scanner(System.in);
                        out = System.out;
                }
                catch (Exception e)
                {
                        return;
                }
               
               
                test();
        }
}

