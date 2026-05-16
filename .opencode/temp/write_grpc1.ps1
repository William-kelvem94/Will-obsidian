$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'

---

## 3. gRPC

Framework de RPC (Remote Procedure Call) desenvolvido pelo Google, usando Protocol Buffers como linguagem de definicao de interface e serializacao.

**Referencia:** gRPC Documentation (grpc.io)

### 3.1 Protocol Buffers (Protobuf)

```protobuf
syntax = "proto3";

package usuarios;

service UsuarioService {
  rpc GetUsuario (GetUsuarioRequest) returns (Usuario);
  rpc ListUsuarios (ListUsuariosRequest) returns (ListUsuariosResponse);
  rpc CriarUsuario (CriarUsuarioRequest) returns (Usuario);
  rpc AtualizarUsuarioStream (stream AtualizaRequest) returns (stream Usuario);
}

message Usuario {
  string id = 1;
  string nome = 2;
  string email = 3;
  int32 idade = 4;
}

message GetUsuarioRequest {
  string id = 1;
}

message ListUsuariosRequest {
  int32 page = 1;
  int32 per_page = 2;
}

message ListUsuariosResponse {
  repeated Usuario usuarios = 1;
  int32 total = 2;
}

message CriarUsuarioRequest {
  string nome = 1;
  string email = 2;
  int32 idade = 3;
}

message AtualizaRequest {
  string id = 1;
  optional string nome = 2;
  optional string email = 3;
}
```

### 3.2 Tipos de Streaming

gRPC oferece 4 tipos de comunicacao:

- **Unary:** Cliente envia 1 request, servidor responde 1 response
- **Server Streaming:** Cliente envia 1 request, servidor responde varios responses
- **Client Streaming:** Cliente envia varios requests, servidor responde 1 response
- **Bidirectional Streaming:** Ambos enviam multiplas mensagens

```python
import grpc
from concurrent import futures
import usuarios_pb2
import usuarios_pb2_grpc

class UsuarioServicer(usuarios_pb2_grpc.UsuarioServiceServicer):
    def GetUsuario(self, request, context):
        usuario = USUARIOS_DB.get(request.id)
        if not usuario:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Usuario nao encontrado")
            return usuarios_pb2.Usuario()
        return usuarios_pb2.Usuario(id=usuario.id, nome=usuario.nome, email=usuario.email)

    def ListUsuarios(self, request, context):
        usuarios = list(USUARIOS_DB.values())
        start = (request.page - 1) * request.per_page
        end = start + request.per_page
        return usuarios_pb2.ListUsuariosResponse(
            usuarios=usuarios[start:end],
            total=len(usuarios)
        )

    def AtualizarUsuarioStream(self, request_iterator, context):
        for req in request_iterator:
            usuario = USUARIOS_DB.get(req.id)
            if usuario:
                if req.HasField("nome"):
                    usuario.nome = req.nome
                if req.HasField("email"):
                    usuario.email = req.email
                yield usuarios_pb2.Usuario(id=usuario.id, nome=usuario.nome, email=usuario.email)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
usuarios_pb2_grpc.add_UsuarioServiceServicer_to_server(UsuarioServicer(), server)
server.add_insecure_port("[::]:50051")
server.start()
server.wait_for_termination()
```
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
