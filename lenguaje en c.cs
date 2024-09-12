using System;
using System.Runtime.Remoting.Messaging;



internal class Program
{


	static double[] x;
	static double areaCirculo(double r)
	{
		return Math.PI * Math.Pow(r, 2);
	}

	static double sumatoria(double[] x)
	{
		int n = x.Length;
		double sigma = 0;
		for (int i = 0; i < n; i++)
		{
			sigma += x[i];
		}
		return sigma;
	}


	static double[] generateArray(doble x1, double xf, double h)
	{
		int n = Convert.ToInt16((xf - x1) / h);
		double[] result = new double[n + 1];
		for (int i = 0; i < n + 1; i++)
		{
			result[i] = x1 + i * h;
		}

		return x;
	}

	static void main(strings[] args)
	{
		x = generateArray(0, 10, 0.1);
		for (int i = 0; i < x.Length; i++)
		{
			Console.WriteLine(x[i]);
		}

		double sigma = sumatoria(x);
		Console.WriteLine("sigma");
		//Console.WriteLine("ingrese el radio");
		//double r= Convert.ToDouble(Console.ReadLine());
		//double area = areaCirculo(r);
		//         Console.WriteLine("A={0}",area);



	}
}

