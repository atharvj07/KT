
import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.awt.geom.Point2D.Double;
import java.util.*;
  
public class Main {
    Scanner sc = new Scanner(System.in);
  
    public static void main(String[] args) {
        new Main(); 
    }
  
    public Main() {
        new aoj0223().doIt();
    }
    class aoj0223{
    	int mx[] = {0,1,0,-1};
    	int my[] = {1,0,-1,0};
    	boolean map[][] = new boolean[53][53];
    	class Par{
    		int x,y;
    		public Par(int x,int y){
    			this.x = x;
    			this.y = y;
    		}
    	}
    	ArrayList<Par> array = new ArrayList<Par>();
    	ArrayList<Par> array2 = new ArrayList<Par>();
    	TreeSet<String> ts = new TreeSet<String>();
    	int roop(int x,int y){
    		for(int i = 0;i < 101;i++){
    			int length = array.size();
//    			System.out.println(i);
    			for(int j = 0;j < length;j++){
    				Par p = array.remove(0);
    				Par p2 = array2.remove(0);
    				int sx = p.x;
    				int sy = p.y;
    				int ex = p2.x;
    				int ey = p2.y;
    				if(sx == ex && sy == ey)return i;
            		for(int k = 0;k < 4;k++){
            			int sx1 = sx;
            			int sy1 = sy;
            			int ex1 = ex;
            			int ey1 = ey;
            			if(sx + mx[k] >= 0 && sx + mx[k] < x
            					&& sy + my[k] >= 0 && sy + my[k] < y){
            				if(map[sy + my[k]][sx + mx[k]]){
            					sx1 = sx + mx[k];
            					sy1 = sy + my[k];
            				}
            			}
            			if(ex - mx[k] >= 0 && ex - mx[k] < x
            					&& ey - my[k] >= 0 && ey - my[k] < y){
            				if(map[ey - my[k]][ex - mx[k]]){
            					ex1 = ex - mx[k];
            					ey1 = ey - my[k];
            				}
            			}
            			String str = sx1+","+sy1+","+ex1+","+ey1;
            			if(ts.add(str)){
//            				System.out.println(str);
    						array.add(new Par(sx1,sy1));
    						array2.add(new Par(ex1,ey1));
    					}
            		}
    			}
    		}
    		return -1;
    	}
        void doIt() {
        	while(true){
        		int X = sc.nextInt();
        		int Y = sc.nextInt();
        		if(X+Y == 0)break;
        		array.add(new Par(sc.nextInt()-1,sc.nextInt()-1));
        		array2.add(new Par(sc.nextInt()-1,sc.nextInt()-1));
        		for(int i = 0;i < Y;i++){
        			for(int j = 0;j < X;j++){
        				map[i][j] = sc.nextInt() == 0 ? true:false ;
        			}
        		}
//        		for(int i = 0;i < Y;i++){
//        			for(int j = 0;j < X;j++){
//        				System.out.print(map[i][j]);
//        			}
//        			System.out.println();
//        		}
        		int num = roop(X,Y);
        		if(num == -1)System.out.println("NA");
        		else System.out.println(num);
        		array.clear();
        		array2.clear();
        		ts.clear();
        	}
    	}
    }
}