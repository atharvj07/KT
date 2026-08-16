import java.util.*;


public class Main {

	Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		new Main().doit();

	}
	
	private void doit(){
		new A();
	}
	
	class A{
		A(){
			while(true){
				int w = sc.nextInt();
				int d = sc.nextInt();
				if((w|d) == 0)break;
				int [] data =new int[w];
				int [] data2 = new int[d];
				int sum = 0;
				for(int i = 0 ; i < w; i++){
					data[i] = sc.nextInt();
					sum += data[i];
				}
				for(int i = 0 ; i < d; i++){
					data2[i] = sc.nextInt();
					sum += data2[i];
				}
				//System.out.println(" sum = " +sum);
				
				boolean [] used = new boolean[w];
				boolean [] used2 = new boolean[d];
				for(int i = 0 ; i < w; i++){
					for(int j = 0 ; j < d; j++){
						if(! used2[j]){
							if(data[i] == data2[j]){
								sum -= data2[j];
								used2[j] = true;
								break;
							}
						}
					}
					//System.out.println("i = " + i+ "sum = " + sum);
				}
				System.out.println(sum);
			}
		}
	}

}