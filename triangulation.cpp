#include <math.h>
#include <stdio.h>

#define THRESHOLD 0.0001

// Given two points, and a guess, the function finds a point for the current position
void getPosition(double x1, double y1, double r1, double x2, double y2, double r2, double gx, double gy)
{
    // find the two probable points using a circle...

    // distance between centers...
    double d = sqrt(abs((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
    printf("%lf\n", y1 - y2);

    // check if two points exist
    if (d > r1 + r2 || d < abs(r1 - r2))
    {
        // circles are separate (or contained)
        printf("No intersection points!!\n");
    }
    else if (d < THRESHOLD)
    {
        // coincident!
        printf("Coincident!");
    }

    double centerDist = (r1 * r1 - r2 * r2 + d * d) / (2 * d);
    double height = sqrt(abs(r1 * r1 - centerDist * centerDist));

    // Evaluate center point
    double cx = x1 + centerDist * (x2 - x1) / d;
    double cy = y1 + centerDist * (y2 - y1) / d;

    // Evaluate postion
    double px1 = cx + height * (y2 - y1) / d;
    double px2 = cx - height * (y2 - y1) / d;
    double py1 = cy - height * (x2 - x1) / d;
    double py2 = cy + height * (x2 - x1) / d;

    // Find the point closest to the guess.
    double d1 = sqrt(abs(((px1 - gx) * (px1 - gx)) + ((py1 - gy) * (py1 - gy))));
    double d2 = sqrt(abs(((px2 - gx) * (px2 - gx)) + ((py2 - gy) * (py2 - gy))));

    if (d1 > d2)
    {
        printf("(x, y) = (%lf, %lf)\n", px2, py2);
    }
    else
    {
        printf("(x, y) = (%lf, %lf)\n", px1, py1);
    }

    printf("%lf and 2: %lf\n", d1, d2);
}

int main()
{
    getPosition(1, 1, 3, 5, 5, 4, 1, 1);
    return 0;
}