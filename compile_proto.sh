
for pt in `find . | grep \\\.proto$ `; \
        do
            python3 -m grpc_tools.protoc -I . -I include/ --python_out=./ --grpc_python_out=./ $pt;
            protoc -I . -I include/ $pt --go_out=paths=source_relative,plugins=grpc:.;
        done