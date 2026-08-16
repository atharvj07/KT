import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.awt.geom.Point2D.Double;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;
import java.lang.Object;
 
public class Main {
    Scanner sc = new Scanner(System.in);
   
    public static void main(String[] args) {
        new Main(); 
    }
   
    public Main() {
        new D().doIt();
    }
    class D{
    	boolean array[][] = new boolean[100][100];
    	ArrayList<ArrayList<Integer>> Ege = new ArrayList<ArrayList<Integer>>();
    	ArrayList<Integer> Node = new ArrayList<Integer>();
    	ArrayList<Integer> subNode = new ArrayList<Integer>();
    	ArrayList<Integer> NotNode = new ArrayList<Integer>();
    	int sum = 0;
    	int max = 0;
    	void clear(){
    		Node.clear();
    		NotNode.clear();
    	}
    	void doIt(){
    		NodeSet();
//    		check();
    		
    		while(true){
    			max = -1000;
    			int n = sc.nextInt();
    			int m = sc.nextInt();
    			clear();
    			if(n + m == 0)break;
    			sum = 0;
    			for(int i = 0;i <= n;i++){
    				sum = sum + i;
    			}
//    			System.out.println(sum);
    			for(int i = 0;i < sum;i++){
    				int num = sc.nextInt();
    				if(num == 0)NotNode.add(i);
    				Node.add(num);
    			}
    			for(int j = 0;j < NotNode.size();j++){
    				Node.set(NotNode.get(j), m);
    				NN(m);
    				Node.set(NotNode.get(j), 0);
    			}
    			System.out.println(max);
    		}
    	}
    	void NN(int m){
    		subNode.clear();
    		for(int i = 0;i < Node.size();i++){
				subNode.add(Node.get(i));
			}
//    		System.out.println(subNode.toString());
//			System.out.println(NotNode.toString());
    		int ncnt = 0;
			for(int i = 0;i < sum;i++){
				if(subNode.get(i) > 0){
//					System.out.println(i+" "+subNode.get(i));
					int cnt = bfs(subNode.get(i),i,sum);
//					System.out.println(i+" "+cnt);
					if(subNode.get(i) == -m)ncnt = ncnt-cnt;
					else ncnt = ncnt + cnt;
				}
			}
			max = Math.max(max,ncnt);
//			System.out.println(ncnt);
//			System.out.println();
    	}
    	int bfs(int num,int index,int sum){
    		ArrayList<Integer> NextNode = new ArrayList<Integer>();
    		NextNode.add(index);
    		subNode.set(index, -num);
    		int cnt = 0;
    		boolean ok = true;
    		while(NextNode.size() > 0){
    			cnt++;
    			index = NextNode.remove(0);
//    			System.out.println("?????¨:"+index);
//    			System.out.println(Ege.get(index).toString());
    			for(int i = 0;i < Ege.get(index).size();i++){
    				int next = Ege.get(index).get(i);
    				if(next < sum){
    					if(subNode.get(next) == num){
    						NextNode.add(next);
    						subNode.set(next, -num);
    					}else if(subNode.get(next) == 0)ok = false;
    				}
    			}
    		}
    		if(ok)return cnt;
    		else return 0;
    	}
    	void NodeSet(){
    		int num = 0;
    		int n = 1;
    		for(int i = 0;i <= 55;i++){
    			if(i != num){
    				array[i][i+1] = true;
    				array[i+1][i] = true;
    			}
    			array[i][i+n] = true;
    			array[i+n][i] = true;
    			array[i][i+n+1] = true;
    			array[i+n+1][i] = true;
    			if(i == num){
    				n++;
    				num = num + n;
    			}
    		}
    		for(int i = 0;i <= 55;i++){
    			ArrayList<Integer> IS = new ArrayList<Integer>();
    			for(int j = 0;j < 55;j++){
    				if(array[i][j])IS.add(j);
    			}
    			Ege.add(IS);
    		}
    	}
    	void check(){
    		for(int i = 0;i < 55;i++){
    			ArrayList<Integer> e = new ArrayList<Integer>();
    			e = Ege.get(i);
    			System.out.println(Ege.toString());
    		}
    	}
    }
}