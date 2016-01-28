import igen
message = open('igen/fixtures/normal_point.bin', 'rb').read()
p = igen.parse(message)
p.report()