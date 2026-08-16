import java.util.*;
public class Main {
	//0418 start
	//0503 cording end
	//0515 find a fatal error and sleep
	//1210 restart
	//1300 sample match WA
	//1320 WA modi {x,x,y,y}patttern
	
	//dice is, 0 = south, 1 = east, 2 = top, 3 = bottom, 4 = west, 5 = north;
	String [] order = {"","n","s", "e", "w", "nn"};
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			HashMap<String, Integer> tonum = new HashMap<String, Integer>();
			int [][] dice = new int[n][6];
			for(int i = 0; i < n; i++){
				for(int j = 0; j < 6; j++){
					String s = sc.next();
					int ind = -1;
					if(tonum.containsKey(s)){
						ind = tonum.get(s);
					}
					else{
						ind = tonum.size() + 1;
						tonum.put(s, ind);
					}
					dice[i][j] = ind;
				}
			}
			
			if(n == 1){
				System.out.println(0);
			}
			else if(n == 2){
				System.out.println(solve(dice));
			}
			else if(n == 3){
				int res = solve3(dice);
				System.out.println(res);
			}
			else{
				int res = solve4(dice);
				System.out.println(res);
			}
			//debug
//			for( String key : tonum.keySet()){
//				System.out.println(key + " " + tonum.get(key));
//			}
		}
	}

	private int solve4(int[][] dice) {
		int [][] work =new int[4][6];
		int res = 1 << 24;
		work[0] = Arrays.copyOf(dice[0], dice[0].length);
		for(int j1 = 0; j1 < order.length; j1++){
			work[1] = Arrays.copyOf(dice[1], dice[1].length);
			for(int i1 = 0; i1 < order[j1].length(); i1++){
				turn(work[1], order[j1].charAt(i1));
			}
			
			for(int i1 = 0; i1 < 4; i1++){
				slide(work[1]);
				
				//2個目
				for(int j2 = 0; j2 < order.length; j2++){
					work[2] = Arrays.copyOf(dice[2], dice[2].length);
					for(int i2 = 0; i2 < order[j2].length(); i2++){
						turn(work[2], order[j2].charAt(i2));
					}
					for(int i2 = 0; i2 < 4; i2++){
						slide(work[2]);
						
						for(int j3 = 0; j3 < order.length; j3++){
							work[3] = Arrays.copyOf(dice[3], dice[3].length);
							for(int i3 = 0; i3 < order[j3].length(); i3++){
								turn(work[3],order[j3].charAt(i3));
							}
							
							for(int i3 = 0; i3 < 4; i3++){
								slide(work[3]);
								
								//ある面に対して、その面の種類が同じであればok
								//setを使って、size - 1の値を足していく
								//その値の足し算が答えとなる
								int sum = 0;
								for(int i = 0; i < 6;i++){
									HashMap<Integer,Integer> s = new HashMap<Integer, Integer>();
									for(int j = 0; j < work.length; j++){
										if(s.containsKey(work[j][i])){
											s.put(work[j][i], s.get(work[j][i]) + 1);
										}
										else{
											s.put(work[j][i], 1);
										}
										
									}
									
									if(s.size() == 2){
										for(int key: s.keySet()){
											if(s.get(key) == 2){
												sum += 2;
												break;
											}
											else{
												sum += 1;
												break;
											}
										}
									}
									else{
										sum += s.size() - 1;
									}
								}
								res = Math.min(sum, res);
							}
						}
					}
				}
				
			}
		}
		return res;
	}

	private int solve3(int[][] dice) {
		int [][] work =new int[3][6];
		int res = 1 << 24;
		work[0] = Arrays.copyOf(dice[0], dice[0].length);
		for(int j1 = 0; j1 < order.length; j1++){
			work[1] = Arrays.copyOf(dice[1], dice[1].length);
			for(int i1 = 0; i1 < order[j1].length(); i1++){
				turn(work[1], order[j1].charAt(i1));
			}
			
			for(int i1 = 0; i1 < 4; i1++){
				slide(work[1]);
				
				//2個目
				for(int j2 = 0; j2 < order.length; j2++){
					work[2] = Arrays.copyOf(dice[2], dice[2].length);
					for(int i2 = 0; i2 < order[j2].length(); i2++){
						turn(work[2], order[j2].charAt(i2));
					}
					for(int i2 = 0; i2 < 4; i2++){
						slide(work[2]);
						
						//ある面に対して、その面の種類が同じであればok
						//setを使って、size - 1の値を足していく
						//その値の足し算が答えとなる
						int sum = 0;
						for(int i = 0; i < 6;i++){
							HashSet<Integer> s = new HashSet<Integer>();
							for(int j = 0; j <  work.length; j++){
								s.add(work[j][i]);
							}
							sum += s.size() - 1;
						}
						res = Math.min(sum, res);
					}
				}
				
			}
		}
		return res;
	}

	private int solve(int[][] dice) {
		int [][] work =new int[2][6];
		int res = 1 << 24;
		work[0] = Arrays.copyOf(dice[0], dice[0].length);
		for(int j1 = 0; j1 < order.length; j1++){
			work[1] = Arrays.copyOf(dice[1], dice[1].length);
			for(int i1 = 0; i1 < order[j1].length(); i1++){
				turn(work[1], order[j1].charAt(i1));
			}
			
			for(int i1 = 0; i1 < 4; i1++){
				slide(work[1]);
				
				//ある面に対して、その面の種類が同じであればok
				//setを使って、size - 1の値を足していく
				//その値の足し算が答えとなる
				int sum = 0;
				for(int i = 0; i < 6;i++){
					HashSet<Integer> s = new HashSet<Integer>();
					for(int j = 0; j <  work.length; j++){
						s.add(work[j][i]);
					}
					sum += s.size() - 1;
				}
				res = Math.min(sum, res);
				
			}
		}
		return res;
	}

	private void slide(int [] dice) {
		swap(dice, 0,4,5,1);
	}

	//dice is, 0 = south, 1 = east, 2 = top, 3 = bottom, 4 = west, 5 = north;
	private void turn(int [] dice, char c) {
		switch(c){
		case 'n':
			swap(dice, 2,5,3,0);
			break;
		
		case 's':
			swap(dice, 2,0,3,5);
			break;
		
		case 'w':
			swap(dice, 2,4,3,1);
			break;
		
		case 'e':
			swap(dice, 2,1,3,4);
			break;
		
		}
	}

	private void swap(int [] dice, int i, int j, int k, int l) {
		int temp = dice[l];
		dice[l] = dice[k];
		dice[k] = dice[j];
		dice[j] = dice[i];
		dice[i] = temp;
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}