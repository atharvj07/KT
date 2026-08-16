import java.io.*;

public class Main {

	public static void main(String[] args) {
		BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
		try {
			int k = Integer.valueOf(r.readLine());
			
			int[] T = new int[65536];
			
			for(int i=0;i<k;i++){
				//read N and string
				int N = Integer.valueOf(r.readLine());
				String str = r.readLine();
				
				//convert string into 2-dimension array w/ 0/1
				int[][] book = new int[N+1][2];
				if(str.charAt(0)=='Y'){
					book[0][0]=1;
				}
				if(str.charAt(2*N)=='Y'){
					book[0][1]=1;
				}
				for(int j=1;j<N;j++){
					if(str.charAt(j*2-1)=='Y'||str.charAt(j*2)=='Y'){
						book[j][0] = 1;
					} else {
						book[j][0] = 0;
					}
					if(str.charAt(j*2-1+2*N)=='Y'||str.charAt(j*2+2*N)=='Y'){
						book[j][1] = 1;
					} else {
						book[j][1] = 0;
					}
				}
				if(str.charAt(2*N-1)=='Y'){
					book[N][0]=1;
				}
				if(str.charAt(4*N-1)=='Y'){
					book[N][1]=1;
				}
				
				int hpos=0, vpos=0, cost=0;
				
				while(hpos<N){
					if(vpos==0){
						if(book[hpos][0]==1 && book[hpos][1]==1){
							cost += 2;
							
							int temp = hpos+1;
							while(temp<N){
								vpos = 0;
								if(book[temp][0]==1||book[temp][1]==1){
									vpos = 1;
									break;
								}
								temp++;
							}
						}
						if(book[hpos][0]==1 && book[hpos][1]==0){
							cost++;
							vpos = 1;
						}
						if(book[hpos][0]==0 && book[hpos][1]==1){
							cost+=2;
							vpos = 1;
						}
					} else if(vpos==1){
						if(book[hpos][0]==0 && book[hpos][1]==1){
							cost++;
							vpos = 1;
						}
						if(book[hpos][0]==1 && book[hpos][1]==1){
							cost += 2;
							
							int temp = hpos+1;
							while(temp<N){
								vpos = 0;
								if(book[temp][0]==1||book[temp][1]==1){
									vpos = 1;
									break;
								}
								temp++;
							}
						}
						if(book[hpos][0]==1 && book[hpos][1]==0){
							cost += 1;
							
							int temp = hpos+1;
							while(temp<N){
								vpos = 0;
								if(book[temp][0]==1||book[temp][1]==1){
									vpos = 1;
									break;
								}
								temp++;
							}
						}
					}
					hpos++;
					cost++;
				}
				
				if(book[N][1]==1){
					cost+=2;
				} else if (book[N][0]==1){
					cost++;
				}
				System.out.println(cost);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}