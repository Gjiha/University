#Eventualmente go mod init assetTransfer
# e in alcuni casi vuole go 1.18
#go install golang.org/dl/go1.18@latest


go1.18 mod tidy
go1.18 mod vendor
go1.18 build -buildmode=c-shared -o assetTransfer.so assetTransfer-c.go
