import java.util.Scanner;

//Mirror Illusion
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		int[][][] g = {
				{{0, 0},{0, 800}},
				{{0, 0},{800, 0}},
				{{0, 800},{800, 800}},
				{{800, 0},{800, 800}}
		};
		for(;;){
			int n = sc.nextInt();
			if(n<0)break;
			int px = 75, py = 25, dx = 1, dy = 1;
			int[][][] wall = new int[n+1][2][2];
			wall[0][0][0] = wall[0][1][0] = 75;
			wall[0][0][1] = wall[0][1][1] = 25;
			for(int i=1;i<=n;i++){
				char ch = sc.next().charAt(0);
				int a = sc.nextInt()*100, b = sc.nextInt()*100;
				if(ch=='x'){
					wall[i][0][0] = a; wall[i][0][1] = b;
					wall[i][1][0] = a+100; wall[i][1][1] = b;
				}
				else{
					wall[i][0][0] = a; wall[i][0][1] = b;
					wall[i][1][0] = a; wall[i][1][1] = b+100;
				}
			}
			for(;;){
				int id = -1, min = 1000;
				for(int i=0;i<=n;i++){
					int x1 = wall[i][0][0], x2 = wall[i][1][0], y1 = wall[i][0][1], y2 = wall[i][1][1];
					if(x1==x2){
						int t = (x1-px)/dx;
						if(t<=0||min<=t)continue;
						int y = py+t*dy;
						if(y1<=y&&y<=y2){
							id = i;
							min = t;
						}
					}
					else{
						int t = (y1-py)/dy;
						if(t<=0||min<=t)continue;
						int x = px+t*dx;
						if(x1<=x&&x<=x2){
							id = i;
							min = t;
						}
					}
				}
				if(id==-1){
					min = 1000;
					for(int i=0;i<4;i++){
						int x1 = g[i][0][0], x2 = g[i][1][0], y1 = g[i][0][1], y2 = g[i][1][1];
						if(x1==x2){
							int t = (x1-px)/dx;
							if(t<=0||min<=t)continue;
							int y = py+t*dy;
							if(y1<=y&&y<=y2)min = t;
						}
						else{
							int t = (y1-py)/dy;
							if(t<=0||min<=t)continue;
							int x = px+t*dx;
							if(x1<=x&&x<=x2)min = t;
						}
					}
					System.out.println((px+min*dx)+" "+(py+min*dy));
					break;
				}
				if(id==0){
					System.out.println("75 25");
					break;
				}
				px+=min*dx; py+=min*dy;
				if(wall[id][0][0]==wall[id][1][0])dx*=-1;
				else dy*=-1;
			}
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}