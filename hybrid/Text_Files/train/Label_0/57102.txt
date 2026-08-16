
import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);

		while(true) {
			int W=in.nextInt(),H=in.nextInt(),n=in.nextInt(),m=in.nextInt();
			if(m==0)break;
			List<List<Integer>> kami=new ArrayList<>();

			for(int i=0;i<H;i++) {
				List<Integer> ls=new ArrayList<>();
				for(int j=0;j<W;j++) {
					ls.add(1);
				}
				kami.add(ls);
			}

			for(int i=0;i<n;i++) {
				int d=in.nextInt(),c=in.nextInt();

				if(d==1) {
					if(c*2>kami.get(0).size()) {
//						System.out.println("escape Overflow X");
						c=kami.get(0).size()-c;
						for(int p=0;p<kami.size();p++) {
							Collections.reverse(kami.get(p));
						}
					}


					for(int p=0;p<kami.size();p++) {
						for(int q=0;q<c;q++) {
							int a=kami.get(p).get(c+q),b=kami.get(p).get(c-1-q);
							kami.get(p).set(c+q, a+b);
						}

						for(int q=0;q<c;q++)kami.get(p).remove(0);
					}
				}
				else {
					if(c*2>kami.size()) {
//						System.out.println("escape Overflow Y");
						c=kami.size()-c;
						Collections.reverse(kami);
					}

					for(int p=0;p<c;p++) {
						for(int q=0;q<kami.get(0).size();q++) {
							int a=kami.get(kami.size()-1-c-p).get(q),
									b=kami.get(kami.size()-c+p).get(q);
							kami.get(kami.size()-1-c-p).set(q, a+b);
						}
					}
					for(int p=0;p<c;p++)kami.remove(kami.size()-1);
				}
				/*System.out.println();
				for(int k=0;k<kami.size();k++) {
					for(int l=0;l<kami.get(k).size();l++) {
						System.out.print(kami.get(k).get(l)+" ");
					}
					System.out.println();
				}*/
			}

			for(int i=0;i<m;i++) {
				int x=in.nextInt(),y=in.nextInt();
				System.out.println(kami.get(kami.size()-1-y).get(x));
			}
			/*System.out.println();
			for(int i=0;i<kami.size();i++) {
				for(int j=0;j<kami.get(i).size();j++) {
					System.out.print(kami.get(i).get(j)+" ");
				}
				System.out.println();
			}*/
		}
		/*System.out.println();
		for(int i=0;i<kami.size();i++) {
			for(int j=0;j<kami.get(i).size();j++) {
				System.out.print(kami.get(i).get(j)+" ");
			}
			System.out.println();
		}*/
	}

}

