import java.util.*;

public class CodeForcesD{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int q = input.nextInt();
		for(int i = 0;i<q;i++){
			int n = input.nextInt();
			int[] a = new int[n];
			int[] arr = new int[n];
			boolean bool = true;
			boolean boolC = true;
			for(int j = 0;j<n;j++){
				a[j] = input.nextInt();
			}
			for(int j = 0;j<a.length-1;j++){
				if(a[j] != a[j+1]){
					boolC = false;
					break;
				}
			}
			if(boolC){
				System.out.println(1);

				for(int j = 0;j<a.length;j++){
					System.out.print(1 + " ");
				}
				System.out.println();
			}
			else{
				if(a.length%2 == 0){
					System.out.println(2);
					for(int j = 0;j<a.length;j++){
						if(j%2 == 0){
							System.out.print(1 + " ");
						}
						else{
							System.out.print(2 + " ");
						}
					}
					System.out.println();
				}
				else{
					arr[0] = 1;
					for(int j = 1;j<a.length;j++){
						if(a[j-1] == a[j] && bool){
							arr[j] = arr[j-1];
							bool = false;
						}
						else{
							if(arr[j-1] == 2){
								arr[j] = 1;
							}
							else{
								arr[j] = 2;
							}
						}
					}
					if(bool){
						if(a[a.length-1] == a[0]){
							arr[arr.length-1] = arr[0];
							System.out.println(2);
						}
						else{
							arr[arr.length-1] = 3;
							System.out.println(3);
						}
						
					}
					else{
						System.out.println(2);
					}

					for(int j = 0;j<arr.length;j++){
						System.out.print(arr[j] + " ");
					}
					System.out.println();
				}
			}
		}	
	}
}