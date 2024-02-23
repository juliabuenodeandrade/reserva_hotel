from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from app.reservations import create_reservation, list_reservations
from app.models import Reservation  # Certifique-se de que este import está correto com base na sua estrutura de diretórios

app = FastAPI(
    title="Reservas de Hotel",
    description="Um sistema simples de reservas de hotel.",
    version="1.0")

@app.post("/reservations/")
def add_reservation(reservation: Reservation):
    """
    Cria uma nova reserva.

    Este endpoint aceita um objeto JSON que representa uma reserva e utiliza
    a função `create_reservation` para adicionar essa reserva ao sistema.

    O corpo da requisição deve seguir o modelo definido pela classe `Reservation`.
    """
    return create_reservation(
        reservation.name, reservation.hotel_name, reservation.check_in, reservation.check_out
    )

@app.get("/reservations/")
def get_reservations():
    """
    Lista todas as reservas existentes.
    """
    return list_reservations()


#redirecionar / para /docs
@app.get("/")
def redirect_to_docs():
    """
    Redireciona a raiz do servidor para a documentação da API.
    """
    return RedirectResponse(url="/docs")

