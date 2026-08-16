import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Main main=new Main();
		main.run();
	}

	public static int h;
	public static int w;
	public static boolean done;

	public static Integer[][] field;

	public static boolean[][] isReached;

	public static Deque<Point> data;



	void run() {

//
//		Scanner sc=null;
//		try {
//			File file=new File("C:\\pleiades\\eclipse\\text\\atcoder.txt");
//
//			sc = new Scanner(file);
//		} catch (FileNotFoundException e) {
//			// TODO 自動生成された catch ブロック
//			e.printStackTrace();
//		}
		Scanner sc=new Scanner(System.in);


		while(true) {
			w=sc.nextInt();
	    	h=sc.nextInt();

	    	if(w==0 && h ==0) {
	    		break;
	    	}

			field=new Integer[h][w];
			isReached=new boolean[h][w];


			for(boolean[] a:isReached) {
				Arrays.fill(a, false);
			}



			for(int i=0;i<h;i++) {
				for(int j=0;j<w;j++) {

					Integer buf=sc.nextInt();
					field[i][j]=buf;

					if(buf.equals(0)) {
						isReached[i][j]=true;
					}

				}
			}

			done=false;

			data=new ArrayDeque<Point>();

			int counter=0;

			while(true) {

				Point buf=getLocateIsNotReached();



				if(buf!=null) {
					data.push(buf);
					counter++;
					dfs();
				}else {
					break;
				}

			}

				System.out.println(counter);
			}

		sc.close();


		}

		void dfs() {
			Point bufPoint=null;

			while(!data.isEmpty()) {

				bufPoint=data.pop();


				int nowY=bufPoint.getY();
				int nowX=bufPoint.getX();

				isReached[nowY][nowX]=true;


				int nextY=0;
				int nextX=0;

				int[] dy= {1,1,0,-1,-1,-1,0,1};
				int[] dx= {0,1,1,1,0,-1,-1,-1,0};

				for(int d=0;d<8;d++) {
					nextY=nowY+dy[d];
					nextX=nowX+dx[d];

					if(canProceed(nextY,nextX)) {
						data.push(new Point(nextY,nextX));
					}
				}

		}

	}

	Point getLocateIsNotReached() {



		for(int i=0;i<h;i++) {
			for(int j=0;j<w;j++) {

				if(!isReached[i][j]) {
					return new Point(i,j);
				}

			}
		}

		return null;
	}



	boolean canProceed(int nextY,int nextX) {

		boolean isInY =nextY>=0 && nextY<h;
		boolean isInX=nextX>=0 && nextX<w;

		boolean isIn=isInY && isInX;

		if(!isIn) {
			return false;
		}

		boolean notWall=!field[nextY][nextX].equals(0);

		return isInY && isInX && notWall && !isReached[nextY][nextX];
	}


}

class Point{
	int y;
	int x;
	/**
	 * @return y
	 */
	public int getY() {
		return y;
	}
	/**
	 * @return x
	 */
	public int getX() {
		return x;
	}
	/**
	 * @param y セットする y
	 */
	public void setY(int y) {
		this.y = y;
	}
	/**
	 * @param x セットする x
	 */
	public void setX(int x) {
		this.x = x;
	}
	public Point(int y, int x) {
		super();
		this.y = y;
		this.x = x;
	}


}
