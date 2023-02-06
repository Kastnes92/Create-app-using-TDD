# inches
inc =15

# millimeters
mm = inc /0.0393700787

# centimeters
cm = inc /0.3937007874

# meters
m = inc /39.37007874

print(
    f"inches({inc}) => Millimeters({round(mm,3)})"
)

print(
    f"inches({inc}) => centimeters({round(cm,3)})"
)
print(
    f"inches({inc}) => meters({round(m,3)})"
)