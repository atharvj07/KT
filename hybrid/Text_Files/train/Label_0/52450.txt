

import java.awt.geom.Point2D;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

//n個の点から凸包を生成するためのプログラム
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		Point2D input[] = new Point2D[n];

		for(int i = 0; i < n; i++){
			String[] tmpArray = br.readLine().split(" ");

			double x = Double.parseDouble(tmpArray[0]);
			double y = Double.parseDouble(tmpArray[1]);

			input[i] = new Point2D.Double(x, y);
		}

		Convex convex = new Convex(input);

		System.out.println(convex.getSize());

		//ここでは一番下から反時計回りの指示
		int start = convex.searchBottom();

		for(int i = 0; i < convex.getSize(); i++){
			printPointAsInt(convex.points[(convex.getSize() + start - i)%convex.getSize()]);
		}
	}

	static void printPointAsInt(Point2D point){
		System.out.println((int)point.getX()+" "+(int)point.getY());
	}

}

class Convex {
	//並び順は一番左から時計回り
	Point2D points[];

	Convex(Point2D[] points){

		//x座標で整列
		Arrays.sort(points, (p1, p2) ->(p1.getX() == p2.getX() ?
				(p1.getY() == p2.getY() ? 0 : (p1.getY() > p2.getY() ? 1 : -1)) :
					(p1.getX() > p2.getX() ? 1 : -1))
				);

		//debug
//		for(int i = 0; i < points.length; i++){
//			System.out.println(points[i].getX()+" "+points[i].getY());
//		}

		ArrayList<Point2D> upper = new ArrayList<Point2D>();
		ArrayList<Point2D> lower = new ArrayList<Point2D>();

		//この2点が上の凸包にあるとする
		upper.add(points[0]);
		upper.add(points[1]);

		for(int i = 2; i < points.length; i++){
			upper.add(points[i]);
//			System.out.println("add "+points[i].getX() + " "+points[i].getY());

			//最後の3点が左回りなら最後から2番目の点を削除
			while(upper.size() >= 3 && crossProduct(upper.get(upper.size() - 3), upper.get(upper.size() - 2), upper.get(upper.size() - 1)) > 0){
				//debug
//				Point2D tmp = upper.get(upper.size() - 2);
//				System.out.println("delete "+tmp.getX()+" "+tmp.getY());
				upper.remove(upper.size() - 2);

//				System.out.println("delete complete. current size "+ upper.size());
			}
		}

		//この2点が下の凸包にあるとする
		lower.add(points[0]);
		lower.add(points[1]);

		for(int i = 2; i < points.length; i++){
			lower.add(points[i]);

			//最後の3点が左回りなら最後から2番目の点を削除
			while(lower.size() >= 3 && crossProduct(lower.get(lower.size() - 3), lower.get(lower.size() - 2), lower.get(lower.size() - 1)) < 0){
				lower.remove(lower.size() - 2);
			}
		}

		this.points = new Point2D[upper.size() + lower.size() - 2];

		//upperとlowerを合成した配列を作る
		for(int i = 0; i < upper.size(); i++){
			this.points[i] = upper.get(i);
		}

		for(int i = 0; i < lower.size() - 2; i++){
			this.points[i + upper.size()] = lower.get(lower.size() - i - 2);
		}

	}

	//正なら左回り、負なら右回り、0なら共線
	private double crossProduct(Point2D p1, Point2D p2, Point2D p3){
		return (p2.getX() - p1.getX())*(p3.getY() - p1.getY()) - (p2.getY() - p1.getY())*(p3.getX() - p1.getX());
	}

	//頂点数を返す
	int getSize(){
		return points.length;
	}

	//一番下（y座標が同じなら左）にある頂点のインデックスを返す
	int searchBottom(){
		int index = 0;
		double x = points[0].getX();
		double y = points[0].getY();

		for(int i = 1; i < points.length; i++){
			if(points[i].getY() < y || (points[i].getY() == y && points[i].getX() < x)){
				index = i;
				x = points[i].getX();
				y = points[i].getY();
			}
		}

		return index;
	}

}
