											import java.math.BigInteger;
											import java.sql.Array;
										    import java.util.ArrayList;
											import java.util.Arrays;
											import java.util.Collection;
											import java.util.Collections;
											import java.util.Comparator;
											import java.util.HashMap;
											import java.util.InputMismatchException;
											import java.util.Iterator;
											import java.util.LinkedHashSet;
											import java.util.LinkedList;
											import java.util.List;
											import java.util.Map;
											import java.util.Map.Entry;	
											import java.util.PriorityQueue;
											import java.util.Queue;
											import java.util.Scanner;
											import java.util.Set;
											import java.util.Stack;
											import java.io.BufferedReader;
											import java.io.IOException;
											import java.io.InputStream;
											import java.io.InputStreamReader;
											import java.util.Scanner;
											import java.util.StringTokenizer;
											import java.util.TreeMap;
											import java.util.TreeSet;
											
											
											
											public class Main {
												
											static long l[];	
											static int k;	
													
												static InputReader rd=new InputReader(System.in);
												public static void main(String[] args) {
													Scanner sc=new Scanner(System.in);
													
													int t=sc.nextInt();
													outer:while(t-->0) {
														
														int n=sc.nextInt();
														int k=sc.nextInt();
														
														StringBuilder sb=new StringBuilder(sc.next());
															
															
														boolean on[]=new boolean[k];
														boolean off[]=new boolean[k];
														
														for(int i=0;i<n;i++) {
															
															if(sb.charAt(i)=='1')on[i%k]=true;
															if(sb.charAt(i)=='0')off[i%k]=true;
															
															
														}
														boolean w=true;
														
														for(int i=0;i<k;i++)if(on[i]&&off[i])w=false;
														int offc=0;int onc=0;
															
														for(int i=0;i<k;i++) {
															if(off[i])offc++;
															if(on[i])onc++;
															
															
														}
														
														
														if(offc*2>k||onc*2>k)w=false;
														
														System.out.println((w)?"YES":"NO");
														
														
														
															}
														
															
													
													
													}
															
															
												public static int removeDuplicateElementsFromArray(int array[], int arrayLength){
											        //Checking the length of the passed array
											        if (arrayLength==0 || arrayLength==1){
											            return arrayLength;
											        }
											        //Creating a temporary array of the passed array lenght
											        int[] temp = new int[arrayLength];
											        int j = 0;
											        //For Loop itteration
											        for (int i=0; i<arrayLength-1; i++){
											            if (array[i] != array[i+1]){
											                temp[j++] = array[i];
											            }
											         }
											        //Setting the last element of array to the temp
											        temp[j++] = array[arrayLength-1];
											        // Changing original array
											        for (int i=0; i<j; i++){
											            array[i] = temp[i];
											        }
											        return j;
											    }	
														
														
													static class Naruto{
														
														int a;int i;
														
														public Naruto(int a ,int i) {
															// TODO Auto-generated constructor stub
														this.a=a;
														this.i=i;
														}
														
													}
													
													
													
													
											
													
												static long power1(long x, long y, long p) 
											    { 
											        // Initialize result 
											        long res = 1;      
											         
											        // Update x if it is more   
											        // than or equal to p 
											        x = x % p;  
											  
											       if (x == 0) return 0; // In case x is divisible by p;    
											  
											        while (y > 0) 
											        { 
											            // If y is odd, multiply x 
											            // with result 
											            if((y & 1)==1) 
											                res = (res * x) % p; 
											      
											            // y must be even now 
											            // y = y / 2 
											            y = y >> 1;  
											            x = (x * x) % p;  
											        } 
											        return res; 
											    } 	
									static void dfs(ArrayList<ArrayList<graph>> g,int v,boolean visited[]) {
										
										visited[v]=true;
										l[k]+=1;
										for(graph j:g.get(v)) {
											if(j.c==0) {
												//System.out.println(v);
												if(!visited[j.v])
												dfs(g,j.v,visited);
											}
											
										}
										
										
									}
												
												
									static class graph{
										int v;int c;
										public graph(int v,int c) {
											// TODO Auto-generated constructor stub
											this.v=v;
											this.c=c;
										
										}
										
									}
												
												
													
												
										static		long fact(long n) {
													
													if(n<=1)return 1;
													else return n*fact(n-1);
												}
												
								 static long maxCrossingSum(long arr[], int l, 
							                                int m, int h) 
							    { 
							        // Include elements on left of mid. 
							       long sum = 0; 
							        long left_sum = Integer.MIN_VALUE; 
							        for (int i = m; i >= l; i--) 
							        { 
							            sum = sum + arr[i]; 
							            if (sum > left_sum) 
							            left_sum = sum; 
							        } 
							  
							        // Include elements on right of mid 
							        sum = 0; 
							        long right_sum = Integer.MIN_VALUE; 
							        for (int i = m + 1; i <= h; i++) 
							        { 
							            sum = sum + arr[i]; 
							            if (sum > right_sum) 
							            right_sum = sum; 
							        } 
							  
							        // Return sum of elements on left 
							        // and right of mid 
							       // returning only left_sum + right_sum will fail for [-2, 1] 
							        return Math.max(left_sum + right_sum, Math.max(left_sum, right_sum)); 
							    } 
							  
							    // Returns sum of maxium sum subarray  
							    // in aa[l..h] 
							    static long maxSubArraySum(long arr[], int l,  
							                                      int h) 
							    { 
							    // Base Case: Only one element 
							    if (l == h) 
							        return arr[l]; 
							  
							    // Find middle point 
							    int m = (l + h)/2; 
							  
							    /* Return maximum of following three  
							    possible cases: 
							    a) Maximum subarray sum in left half 
							    b) Maximum subarray sum in right half 
							    c) Maximum subarray sum such that the  
							    subarray crosses the midpoint */
							    return Math.max(Math.max(maxSubArraySum(arr, l, m), 
							                    maxSubArraySum(arr, m+1, h)), 
							                    maxCrossingSum(arr, l, m, h)); 
							    } 
												
												static long abs(long a) {
													return Math.abs(a);
												}
												
												static class seg{
													
													int x;int y;int l;
													public seg(int x,int y,int l) {
														this.x=x;
														this.y=y;
														this.l=l;
														// TODO Auto-generated constructor stub
													}
													
													
												}
											static	boolean isPresent(int j,int p) {
													
													int i=(j/50)%475;
													
													for(int k=0;k<25;k++) {
													    i = (i * 96 + 42)% 475;
													    if(26+i==p)return true;
														}
													return false;
													
												}
																				
												static class Helper{
													int val;int index;
													public Helper(int  val,int index) {
														
														this.val=val;
														this.index=index;
														// TODO Auto-generated constructor stub
													}
												}
											
										
												
								
											    static boolean isPrime(int n) 
											    { 
											        // Corner cases 
											        if (n <= 1) 
											            return false; 
											        if (n <= 3) 
											            return true; 
											  
											        // This is checked so that we can skip 
											        // middle five numbers in below loop 
											        if (n % 2 == 0 || n % 3 == 0) 
											            return false; 
											  
											        for (int i = 5; i * i <= n; i = i + 6) 
											            if (n % i == 0 || n % (i + 2) == 0) 
											                return false; 
											  
											        return true; 
											    } 
										
												      
												    /* Iterative Function to calculate 
												       (x^y)%p in O(log y) */
												    static long power(long x, long y, long p) 
												    { 
												        // Initialize result 
												        long res = 1;      
												         
												        // Update x if it is more   
												        // than or equal to p 
												        x = x % p;  
												  
												       if (x == 0) return 0; // In case x is divisible by p;    
												  
												        while (y > 0) 
												        { 
												            // If y is odd, multiply x 
												            // with result 
												            if((y & 1)==1) 
												                res = (res * x) % p; 
												      
												            // y must be even now 
												            // y = y / 2 
												            y = y >> 1;  
												            x = (x * x) % p;  
												        } 
												        return res; 
												    } 
									
												
												
												
												  static class InputReader {
												        private InputStream stream;
												        private byte[] buf = new byte[1024];
												        private int curChar;
												        private int numChars;
												        private SpaceCharFilter filter;
											
												        public InputReader(InputStream stream) {
												            this.stream = stream;
												        }
											
												        public int read() {
												            if (numChars == -1)
												                throw new InputMismatchException();
												            if (curChar >= numChars) {
												                curChar = 0;
												                try {
												                    numChars = stream.read(buf);
												                } catch (IOException e) {
												                    throw new InputMismatchException();
												                }
												                if (numChars <= 0)
												                    return -1;
												            }
												            return buf[curChar++];
												        }
											
												        public int readInt() {
												            int c = read();
												            while (isSpaceChar(c))
												                c = read();
												            int sgn = 1;
												            if (c == '-') {
											    sgn = -1;
											    c = read();
											}
											int res = 0;
											do {
											    if (c < '0' || c > '9')
											        throw new InputMismatchException();
											    res *= 10;
											    res += c - '0';
											        c = read();
											    } while (!isSpaceChar(c));
											    return res * sgn;
											}
											
											public String readString() {
											    int c = read();
											    while (isSpaceChar(c))
											        c = read();
											    StringBuilder res = new StringBuilder();
											    do {
											        res.appendCodePoint(c);
											        c = read();
											    } while (!isSpaceChar(c));
											    return res.toString();
											}
											
											public boolean isSpaceChar(int c) {
											    if (filter != null)
											        return filter.isSpaceChar(c);
											    return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
												        }
											
												        public String next() {
												            return readString();
												        }
											
												    }
												
												  public interface SpaceCharFilter {
												        public boolean isSpaceChar(int ch);
												    }	
												
												
																					
																					
																					
																		
											}
											    